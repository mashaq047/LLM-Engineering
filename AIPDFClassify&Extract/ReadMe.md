## AI PDF Classify & Extract

**Classify & Extract** is a local AI-powered assistant built with **Gradio**, **Ollama**, and **LLaMA 3.2** that can:

- Preview uploaded PDF documents  
- Classify whether the document is an **Invoice** or a **Statement**  
- Extract important fields into a **predefined structured JSON format**  
- Validate the extracted data against a JSON Schema

---

#### Features
- 📄 **PDF Preview** – See the uploaded document before processing.
- 🧠 **Local AI Processing** – Uses **Ollama** and **LLaMA 3.2** running locally at `http://localhost:11434/v1`.
- 🔍 **Document Classification** – Detects if the document is an invoice or statement.
- 📊 **Structured Data Extraction** – Outputs key fields (e.g., vendor, invoice number, dates, line items).
- ✅ **Schema Validation** – Ensures the AI output matches the expected JSON structure.

---

#### Tech Stack
- **Python 3.10+**
- [Gradio](https://gradio.app/) – Web UI
- [PyMuPDF](https://pymupdf.readthedocs.io/) – PDF preview & text extraction
- [Ollama](https://ollama.com/) – Local LLaMA model hosting
- [JSON Schema](https://json-schema.org/) – Validation

---

#### Installation

#### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/docdetect-extract.git
cd docdetect-extract
```