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
