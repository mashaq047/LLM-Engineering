import re
import io
import json
import pdfplumber
from PIL import Image
import requests
import gradio as gr
from jsonschema import validate, ValidationError
import pytesseract
import fitz

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# === CONFIG ===
OLLAMA_URL = "http://localhost:11434/v1/chat/completions"  # Ollama OpenAI-compatible API
MODEL_NAME = "llama3.2"  # or "llama3.2-instruct" if that's what you pulled
MAX_TOKENS = 2048

USE_OCR_THRESHOLD = 0.4  # if extracted text shorter than this fraction of pages, try OCR

# === JSON SCHEMAS ===
INVOICE_SCHEMA = {
    "type": "object",
    "properties": {
        "doc_type": {"type": "string", "enum": ["invoice", "statement"]},
        "vendor": {"type": ["string", "null"]},
        "invoice_number": {"type": ["string", "null"]},
        "invoice_date": {"type": ["string", "null"], "format": "date"},
        "due_date": {"type": ["string", "null"], "format": "date"},
        "currency": {"type": ["string", "null"]},
        "total_amount": {"type": ["number", "null"]},
        "tax_amount": {"type": ["number", "null"]},
        "line_items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "description": {"type": ["string", "null"]},
                    "quantity": {"type": ["number", "null"]},
                    "unit_price": {"type": ["number", "null"]},
                    "amount": {"type": ["number", "null"]}
                },
                "required": ["description", "quantity", "unit_price", "amount"]
            }
        },
        "billing_address": {
            "type": "object",
            "properties": {
                "street": {"type": ["string", "null"]},
                "city": {"type": ["string", "null"]},
                "state": {"type": ["string", "null"]},
                "zip": {"type": ["string", "null"]},
                "country": {"type": ["string", "null"]}
            },
            "required": ["street", "city", "state", "zip", "country"]
        },
        "shipping_address": {
            "type": "object",
            "properties": {
                "street": {"type": ["string", "null"]},
                "city": {"type": ["string", "null"]},
                "state": {"type": ["string", "null"]},
                "zip": {"type": ["string", "null"]},
                "country": {"type": ["string", "null"]}
            },
            "required": ["street", "city", "state", "zip", "country"]
        },
        "payment_terms": {"type": ["string", "null"]},
        "raw_text": {"type": ["string", "null"]},
        "confidence": {"type": ["number", "null"]}
    },
    "required": [
        "doc_type",
        "vendor",
        "invoice_number",
        "invoice_date",
        "currency",
        "total_amount",
        "line_items",
        "billing_address",
        "shipping_address",
        "raw_text",
        "confidence"
    ]
}


STATEMENT_SCHEMA = {
    "type": "object",
    "required": ["doc_type", "raw_text", "confidence"],
    "properties": {
        "doc_type": {"type": "string"},
        "account_number": {"type": "string"},
        "period_start": {"type": "string"},
        "period_end": {"type": "string"},
        "opening_balance": {"type": ["number", "null"]},
        "closing_balance": {"type": ["number", "null"]},
        "currency": {"type": "string"},
        "transactions": {"type": "array"},
        "raw_text": {"type": "string"},
        "confidence": {"type": "number"}
    }
}

# === PDF Extraction ===
def extract_text_from_pdf_bytes(pdf_bytes):
    text_acc = []
    num_pages = 0
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        num_pages = len(pdf.pages)
        for pg in pdf.pages:
            txt = (pg.extract_text() or "").strip()
            text_acc.append(txt)
    return "\n\n".join(text_acc), num_pages

def ocr_pdf_bytes(pdf_bytes):
    text_acc = []
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        for pg in pdf.pages:
            im = pg.to_image(resolution=200).original
            txt = pytesseract.image_to_string(im)
            text_acc.append(txt)
    return "\n\n".join(text_acc)

def clean_text_for_prompt(text, max_chars=12000):
    text = re.sub(r'\s+', ' ', text).strip()
    if len(text) > max_chars:
        return text[:max_chars]
    return text

# === Prompt Template ===
PROMPT_TEMPLATE = """
You are a precise extractor. Given the raw text of a single document, determine whether it is an "invoice" or a "statement".
Produce output **ONLY** as a single valid JSON object (no explanatory text) that matches one of the two predefined schemas.

If it's an invoice, return keys: doc_type (invoice), vendor, invoice_number, invoice_date, due_date, currency, total_amount, tax_amount, line_items (list of objects with description, quantity, unit_price, amount), billing_address, shipping_address, payment_terms, raw_text, confidence.

If it's a statement, return keys: doc_type (statement), account_number, period_start, period_end, opening_balance, closing_balance, currency, transactions (list with date, description, amount, balance), raw_text, confidence.

Rules:
- Use ISO-like date strings when possible (YYYY-MM-DD) but any sensible date string is OK.
- numeric fields should be numbers (no currency symbols). If unknown, use null.
- confidence must be a number between 0.0 and 1.0.
- raw_text must contain a short excerpt (up to 1000 chars) of the document text or the full text if short.
- If fields cannot be determined, set them to null or empty list.
- Do NOT output any explanation or additional keys.

Here is the document text (be concise but preserve structure):
<<<DOCUMENT_TEXT>>>
"""

def build_prompt(doc_text):
    return PROMPT_TEMPLATE.replace("<<<DOCUMENT_TEXT>>>", doc_text)

# === Ollama Call ===
def call_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0,
        "max_tokens": MAX_TOKENS
    }
    resp = requests.post(OLLAMA_URL, json=payload)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"].strip()

# === JSON Parsing & Validation ===
def parse_json_str(s):
    s = s.strip()
    match = re.search(r'(\{.*\})', s, flags=re.DOTALL)
    if match:
        s = match.group(1)
    try:
        return json.loads(s)
    except Exception as e:
        s2 = re.sub(r',\s*([}\]])', r'\1', s)
        return json.loads(s2)

def validate_and_normalize(data):
    doc_type = data.get("doc_type", "").lower()
    if doc_type.startswith("inv"):
        validate(instance=data, schema=INVOICE_SCHEMA)
    elif doc_type.startswith("stat"):
        validate(instance=data, schema=STATEMENT_SCHEMA)
    else:
        if "invoice_number" in data or "line_items" in data:
            validate(instance=data, schema=INVOICE_SCHEMA)
        else:
            validate(instance=data, schema=STATEMENT_SCHEMA)
    return data

# === Main Processing ===
def process_pdf_and_extract(pdf_file_bytes):
    text, pages = extract_text_from_pdf_bytes(pdf_file_bytes)
    if len(text.strip()) < 200 and pages > 0:
        ocr_text = ocr_pdf_bytes(pdf_file_bytes)
        if len(ocr_text.strip()) > len(text.strip()):
            text = ocr_text

    text_for_prompt = clean_text_for_prompt(text, max_chars=8000)
    prompt = build_prompt(text_for_prompt)
    raw_output = call_ollama(prompt)

    try:
        parsed = parse_json_str(raw_output)
        validated = validate_and_normalize(parsed)
    except Exception as e:
        return {"error": str(e), "raw_model_output": raw_output}

    if "raw_text" not in validated or not validated["raw_text"]:
        validated["raw_text"] = text_for_prompt[:1000]
    return validated

# === Gradio UI ===
def run_pipeline(file):
    if file is None:
        return {"error": "No file provided."}
    with open(file.name, "rb") as f:
        pdf_bytes = f.read()
    result = process_pdf_and_extract(pdf_bytes)
    return json.dumps(result, indent=2)

def preview_pdf(file):
    if file is None:
        return None
    doc = fitz.open(file.name)
    page = doc[0]  # First page
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Zoom x2
    image_path = "preview.png"
    pix.save(image_path)
    return image_path


# with gr.Blocks() as demo:
#     gr.Markdown("# Ollama Llama 3.2 Invoice/Statement Extractor")
#     with gr.Row():
#         with gr.Column():
#             pdf_in = gr.File(label="Upload PDF (invoice or bank statement)")
#             pdf_preview = gr.Image(label="Preview (First Page)")
#         btn = gr.Button("Analyze")
#         out_text = gr.Textbox(label="Structured JSON output", lines=20)
#     pdf_in.change(preview_pdf, inputs=pdf_in, outputs=pdf_preview)
#     btn.click(fn=run_pipeline, inputs=[pdf_in], outputs=[out_text])


# if __name__ == "__main__":
#     demo.launch( share=False)


with gr.Blocks() as demo:
    gr.Markdown("## AI Invoice/Statement JSON Extractor")

    with gr.Row():
        # Left panel
        with gr.Column(scale=5):
            pdf_in = gr.File(
                label="📤 Upload PDF",
                file_types=[".pdf"]
            )
            pdf_preview = gr.Image(
                label="👁 Preview (First Page)"
            )

        # Center panel (convert button)
        with gr.Column(scale=1, min_width=80, elem_id="center-btn"):
            btn = gr.Button("➡️ Convert", size="lg")

        # Right panel
        with gr.Column(scale=6):
            out_text = gr.Textbox(
                label="📦 Structured JSON Output",
                lines=20,
                interactive=False
            )

    # Events
    pdf_in.change(preview_pdf, inputs=pdf_in, outputs=pdf_preview)
    btn.click(fn=run_pipeline, inputs=[pdf_in], outputs=[out_text])

# Optional CSS for centering button vertically
demo.css = """
#center-btn {
    display: flex;
    align-items: center;
    justify-content: center;
}
"""

demo.launch()
