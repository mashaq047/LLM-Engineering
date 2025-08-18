# 🧠 LLM-Engineering

Welcome to **LLM-Engineering** — a personal collection of AI/LLM-powered projects built to explore, experiment, and engineer real-world applications using large language models. This repository serves as a showcase of practical implementations, ranging from web automation to knowledge processing — all powered by modern LLMs like LLaMA 3, via local or API-based interfaces.

> ⚙️ Built with a strong focus on clean code, practical use cases, and minimal dependencies.

---

## 📦 Projects

### 1. 🕸️ AI Website Summarizer

#### Description

**AI Website Summarizer** is a simple web application that allows users to input any website URL and get a clean, concise summary of the site's content — powered by a locally running LLM via Ollama.

> Think of it as ChatGPT, but for any website, and running entirely on your machine.

#### 🔑 Features

- FastAPI backend + HTML/CSS frontend
- BeautifulSoup used to scrape and clean content
- OpenAI-compatible LLaMA 3 model via [Ollama](https://ollama.com/)
- Markdown + typing animation for responses
- Futuristic UI with reset and re-summarize functionality

#### 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/your-username/LLM-Engineering.git
cd LLM-Engineering/website-summarizer

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the Ollama model
ollama run llama3

# Run the backend
uvicorn main:app --reload
```

### 🛍️ Project 2: Store Assistant AI Chatbot

#### Description

This project is a simple AI-powered chatbot designed to assist customers in a clothing store. The assistant helps answer customer queries strictly related to the store and gently encourages the purchase of discounted items—especially hats, which are 60% off!

The chatbot uses [OpenAI-compatible](https://platform.openai.com/docs/api-reference/chat) models (e.g., `llama3.2`) running locally via [Ollama](https://ollama.com), and is served through an interactive Gradio interface.

---

#### 💡 Features

- AI-powered chatbot for clothing store assistance.
- Highlights promotional items: 
  - 🧢 Hats – 60% off!
  - 👕 Most other items – 50% off.
- Responds only to store-related questions.
- Politely deflects unsupported queries (e.g., "Do you sell belts?").
- Encourages upselling where appropriate.

---

#### 🔧 Requirements

- Python 3.8+
- [Ollama](https://ollama.com) running locally with a model like `llama3.2`
- Required Python packages:
  - `openai`
  - `gradio`

### 📦 Installation

```bash
pip install -r requirements.txt
```

### Project #3 – DocDetect & Extract

**DocDetect & Extract** is a local AI-powered assistant built with **Gradio**, **Ollama**, and **LLaMA 3.2** that can:

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



### Project 3 – AI Farming Advisor (LLM + Quantization + Edge Deployment)

#### 📌 Overview
This project demonstrates how to **run a quantized Large Language Model (LLM) on resource-constrained devices** such as laptops, smartphones, or small edge devices.  
It uses the **Microsoft Phi-3 Mini Instruct** model with **8-bit quantization** (via `bitsandbytes`) to make inference lighter and faster, while maintaining useful performance.  

The chatbot is designed as an **AI Farming Advisor** that can give contextual answers, enhanced by **real-time location and weather data**.  

---

#### 🎯 Key Features
- ✅ **Quantization (8-bit)** for optimized model loading on GPUs/CPUs with graceful fallbacks  
- ✅ **Custom System Prompt** → “AI Farming Advisor”  
- ✅ **Context Integration** → Uses IP-based location + OpenWeatherMap API for real-time weather info  
- ✅ **Streaming Chat UI** → Built with **Gradio** for a responsive chatbot experience  
- ✅ **Lightweight Deployment** → Potential to run on smaller devices (edge AI vision)  

---

#### ⚙️ Tech Stack
- [Transformers](https://huggingface.co/docs/transformers) – Model loading & inference  
- [Bitsandbytes](https://github.com/TimDettmers/bitsandbytes) – 8-bit quantization  
- [Torch](https://pytorch.org/) – Model execution (GPU/CPU)  
- [Gradio](https://gradio.app/) – Interactive chatbot UI  
- [Geocoder](https://geocoder.readthedocs.io/) – Location detection  
- [OpenWeatherMap API](https://openweathermap.org/api) – Weather integration  

---

#### 🚀 Pipeline
1. **Install Dependencies**  
   ```bash
   pip install torch transformers accelerate bitsandbytes gradio sentencepiece requests geocoder
```