
import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from dotenv import load_dotenv

load_dotenv()

# Set up your Google API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
assert GOOGLE_API_KEY, "Please set your GOOGLE_API_KEY in the .env file"

# Choose your document
# You can switch between PDF, TXT, or CSV loaders
def load_documents():
    pdf_path = "bank_policies.pdf"
    txt_path = "bank_policies.txt"
    csv_path = "bank_policies.csv"

    if os.path.exists(pdf_path):
        loader = PyPDFLoader(pdf_path)
    elif os.path.exists(txt_path):
        loader = TextLoader(txt_path)
    elif os.path.exists(csv_path):
        loader = CSVLoader(csv_path)
    else:
        raise FileNotFoundError("No input policy file found!")

    documents = loader.load()
    return documents

# Split documents into manageable chunks
def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_documents(documents)

# Embed using Google Gemini Embeddings
def embed_chunks(chunks):
    embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)
    vectorstore = FAISS.from_documents(chunks, embedding_model)
    vectorstore.save_local("vectorstore")
    print("✅ Vectorstore saved at ./vectorstore")

if __name__ == "__main__":
    print("📥 Loading documents...")
    docs = load_documents()

    print("✂️ Splitting into chunks...")
    chunks = chunk_documents(docs)

    print("🔗 Generating embeddings...")
    embed_chunks(chunks)
