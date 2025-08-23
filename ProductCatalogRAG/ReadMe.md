## 🛒 Product Catalog RAG Chatbot

This project is a **Retrieval-Augmented Generation (RAG) chatbot** built with **LangChain**, **ChromaDB**, **Ollama**, and **Gradio**.  
It allows you to upload a **product catalog** (in `.txt` or `.md` format), embed it into a **vector store**, and then query the catalog in natural language through a chat interface.

---

## 🚀 Features
- 📂 **Document ingestion** (`.txt`, `.md`, `.pdf` supported)  
- 🧩 **Text chunking** with `RecursiveCharacterTextSplitter`  
- 🧠 **Embeddings** using `sentence-transformers/all-MiniLM-L6-v2`  
- 💾 **Vector database** with ChromaDB (persisted locally)  
- 🤖 **Chat LLM** powered by **Ollama** (default: `llama3.2`)  
- 💬 **Conversational memory** for context-aware chat  
- 🌐 **Web UI** via Gradio  

---

## 🏗️ Project Structure

```
ProductCatalogRAG/
│── catalog_docs/        # Place your .txt/.md/ product catalog files here
│── chroma_products/     # ChromaDB persistence directory
│── main.py              # Main application code
│── README.md            # Documentation
```

---

## ⚙️ Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ProductCatalogRAG.git
cd ProductCatalogRAG
```

### 2. Install Dependencies
Make sure you have **Python 3.10+** installed.

Install the required Python packages:
```bash
pip install -r requirements.txt
```

Or install directly:
```bash
pip install langchain langchain-community langchain-core langchain-text-splitters     chromadb transformers sentence-transformers gradio unstructured pypdf
```

### 3. Install & Run Ollama
This project uses **Ollama** to run LLMs locally.  

- [Download Ollama](https://ollama.ai/) and install it.  
- Pull the model used in this project:

```bash
ollama pull llama3.2
```

By default, Ollama runs on `http://localhost:11434`.

---

## ▶️ Running the App

1. Place your catalog files inside:
   ```
   ProductCatalogRAG/catalog_docs/
   ```

2. Run the app:
   ```bash
   python main.py
   ```

3. A **Gradio chat interface** will open in your browser automatically. 🎉

---

## 💡 Example Queries
- *“List all laptops under $1500.”*  
- *“Which headphones have noise cancellation?”*  
- *“Show me the specs of iPhone 16 Pro.”*  

---

## 🔧 Configuration

You can configure the app with environment variables:

| Variable         | Default Value                           | Description                           |
|------------------|-----------------------------------------|---------------------------------------|
| `CATALOG_DIR`    | `./ProductCatalogRAG/catalog_docs`      | Folder containing product docs        |
| `CHROMA_PERSIST` | `./ProductCatalogRAG/chroma_products`   | ChromaDB persistence directory        |
| `EMBEDDING_MODEL`| `sentence-transformers/all-MiniLM-L6-v2`| Embedding model for vector DB         |

---

## 📌 Notes
- Ensure your **Ollama server** is running before launching the chatbot.  
- Supported models: you can swap `llama3.2` with any Ollama-supported LLM (e.g., `mistral`, `gemma`, `phi3`).  
- For larger catalogs, consider changing `chunk_size` in the code.  

