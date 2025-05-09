from loadpdfs import load_full_resumes_from_pdfs
from langchain.vectorstores import Chroma #vector store from langchain where documents are stored as vectors 
from langchain.embeddings import OpenAIEmbeddings #converts text into embeddings using openai's models
import os
import shutil 
from secret_key import secret_key
from langchain.text_splitter import RecursiveCharacterTextSplitter

def create_db():
    db_path = "db_new"
    
    # Always remove old DB
    if os.path.exists(db_path):
        shutil.rmtree(db_path)
        print("🧹 Cleared existing vector database.")
    print(db_path)
    # Load resumes and create new DB
    docs = load_full_resumes_from_pdfs("manifestos")
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    #Breaks long texts into 1000-character chunks with 200 characters overlapping between chunks (to preserve context).
    docs_chunked = splitter.split_documents(docs)
    
    #Uses OpenAI to convert each chunk of text into a numerical vector that captures semantic meaning.
    embedding = OpenAIEmbeddings(openai_api_key=secret_key)
    db = Chroma.from_documents(docs_chunked, embedding, persist_directory=db_path)
    db.persist()

    print("✅ New vector database created.")
    return db