from loadpdfs import load_full_resumes_from_pdfs
from langchain.vectorstores import Chroma #vector store from langchain where documents are stored as vectors 
from langchain.embeddings import OpenAIEmbeddings #converts text into embeddings using openai's models
import os
import shutil 
from secret_key import secret_key

def create_db():
    db_path = "db_new"
    
    # Always remove old DB
    if os.path.exists(db_path):
        shutil.rmtree(db_path)
        print("🧹 Cleared existing vector database.")
    print(db_path)
    # Load resumes and create new DB
    docs = load_full_resumes_from_pdfs("manifestos")
    embedding = OpenAIEmbeddings(openai_api_key=secret_key)
    db = Chroma.from_documents(docs, embedding, persist_directory=db_path)
    db.persist()

    print("✅ New vector database created.")
    return db