# 🧠 LLM-Engineering

Welcome to My **LLM-Engineering** Repo — a personal collection of AI/LLM-powered projects built to explore, experiment, and engineer real-world applications using large language models. This repository serves as a showcase of practical implementations, ranging from web automation to knowledge processing — all powered by modern LLMs like LLaMA 3, via local or API-based interfaces.

> ⚙️ Built with a strong focus on clean code, practical use cases, and minimal dependencies.

---

## 📦 Projects

### 🕸️ Project #1: AI Website Summarizer

#### 📌 Description
**AI Website Summarizer** is a simple web application that allows users to input any website URL and get a clean, concise summary of the site's content — powered by a locally running LLM via Ollama.

> Think of it as ChatGPT, but for any website, and running entirely on your machine.

### 🛍️ Project #2: Store Assistant AI Chatbot

#### 📌 Description
This project is a simple AI-powered chatbot designed to assist customers in a clothing store. The assistant helps answer customer queries strictly related to the store and gently encourages the purchase of discounted items—especially hats, which are 60% off!

The chatbot uses [OpenAI-compatible](https://platform.openai.com/docs/api-reference/chat) models (e.g., `llama3.2`) running locally via [Ollama](https://ollama.com), and is served through an interactive Gradio interface.


### Project #3 – AI PDF Classify & Extract

#### 📌 Description
**AI PDF Classify & Extract** is a local AI-powered assistant built with **Gradio**, **Ollama**, and **LLaMA 3.2** that can:

- Preview uploaded PDF documents  
- Classify whether the document is an **Invoice** or a **Statement**  
- Extract important fields into a **predefined structured JSON format**  
- Validate the extracted data against a JSON Schema


### Project #4 – AI Farming Advisor (LLM + Quantization + Edge Deployment)

#### 📌 Description
This project demonstrates how to **run a quantized Large Language Model (LLM) on resource-constrained devices** such as laptops, smartphones, or small edge devices.  
It uses the **Microsoft Phi-3 Mini Instruct** model with **8-bit quantization** (via `bitsandbytes`) to make inference lighter and faster, while maintaining useful performance.  


### 🛒 Project #5 – Product Catalog RAG Chatbot

#### 📌 Description
This project is a **Retrieval-Augmented Generation (RAG) chatbot** built with **LangChain**, **ChromaDB**, **Ollama**, and **Gradio**.  
It allows you to upload a **product catalog** (in `.txt` or `.md` format), embed it into a **vector store**, and then query the catalog in natural language through a chat interface.
