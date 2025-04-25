import os
from langchain.document_loaders import PyPDFLoader #read and load text from pdf files
from langchain.schema import Document #wraps text content with optional metadata

def load_full_resumes_from_pdfs(pdf_folder): 
    all_docs = [] #Initializes an empty list to store the processed resume documents.
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):  #loops through to process only pdfs
            loader = PyPDFLoader(os.path.join(pdf_folder, filename))   #Creates a PyPDFLoader object using the full file path.
            pages = loader.load() #loads the pages of the pdf and returns a list of document objects, one per page
            full_text = "\n".join([page.page_content for page in pages])   #combines the text from all pages into a single string with newlines between pages
            all_docs.append(Document(page_content=full_text, metadata={"source": filename})) #creates a new document with the entire text of the resume and saves filename for future reference
            print(len(all_docs))
    return all_docs


