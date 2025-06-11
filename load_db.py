from langchain.vectorstores import Chroma #vector store from langchain where documents are stored as vectors 
from langchain.embeddings import OpenAIEmbeddings #converts text into embeddings using openai's models
from secret_key import secret_key

db_path = "./chroma.db"

def load_db():
    
    embedding = OpenAIEmbeddings(openai_api_key=secret_key)
    
    db = Chroma(persist_directory=db_path,embedding_function=embedding) #loads chroma db from disk and connects it to embedding function so that it can process new queries
    
    return db
    
 
