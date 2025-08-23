### 🛍️ Store Assistant AI Chatbot

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