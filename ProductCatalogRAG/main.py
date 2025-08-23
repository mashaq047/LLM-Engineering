
import os
from typing import List

# LangChain + Chroma
from langchain_community.document_loaders import TextLoader, PyPDFLoader, UnstructuredMarkdownLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.chat_models import ChatOllama
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
# LLMs
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline

# UI
import gradio as gr

# ---------- Config ----------
CATALOG_DIR = os.environ.get("CATALOG_DIR", "./ProductCatalogRAG/catalog_docs")
PERSIST_DIR = os.environ.get("CHROMA_PERSIST", "./ProductCatalogRAG/chroma_products")
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
MAX_NEW_TOKENS = 512

# ---------- Document Loading ----------

def load_documents(folder: str) -> List[Document]:
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
        raise FileNotFoundError(f"No catalog docs found in {folder}. Please add .txt, .md, or .pdf files.")

    docs = []
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if file.endswith(".txt"):
            loader = TextLoader(path)
            docs.extend(loader.load())
        elif file.endswith(".md"):
            loader = UnstructuredMarkdownLoader(path)
            docs.extend(loader.load())
    return docs

# ---------- Embeddings + Vector Store ----------

def build_vectorstore(docs: List[Document]):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = splitter.split_documents(docs)
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vectordb = Chroma.from_documents(splits, embeddings, persist_directory=PERSIST_DIR)
    vectordb.persist()
    return vectordb

# ---------- Main App ----------

def main():
    docs = load_documents(CATALOG_DIR)
    vectordb = build_vectorstore(docs)

    llm = ChatOllama(
    model="llama3.2",  # make sure you've pulled it with: ollama pull llama3.2
    base_url="http://localhost:11434",  # Ollama server URL
    temperature=0.3
    )

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    retriever = vectordb.as_retriever()

    conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory
    )

    # set up a new conversation memory for the chat
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    # putting it together: set up the conversation chain with the GPT 4o-mini LLM, the vector store and memory
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory)

    def chat(message, history):
        result = conversation_chain.invoke({"question": message})
        return result["answer"]
    
    view = gr.ChatInterface(chat, type="messages").launch(inbrowser=True)

if __name__ == "__main__":
    main()
