from loadpdfs import load_full_manifestos_from_pdfs
from langchain.vectorstores import Chroma #vector store from langchain where documents are stored as vectors 
from langchain.embeddings import OpenAIEmbeddings #converts text into embeddings using openai's models
import os
import shutil #built in python module to handle file system operations
from secret_key import secret_key
from langchain.text_splitter import RecursiveCharacterTextSplitter

db_path = "./chroma.db"

#in the event where i am uploading new documents, i just have to delete the chroma db folder and run this script again 

def create_db():
    
    docs = load_full_manifestos_from_pdfs("manifestos")
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    docs_chunked = splitter.split_documents(docs)
    
    embedding = OpenAIEmbeddings(openai_api_key=secret_key)
    db = Chroma.from_documents(docs_chunked, embedding, persist_directory=db_path)
    db.persist()
    print("chroma vector database created")
    
    