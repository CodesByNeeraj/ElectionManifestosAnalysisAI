from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_documents_with_overlap(query, db, top_k=2):
    #Perform similarity search to retrieve top-k documents related to the query
    docs_with_metadata = db.similarity_search(query, k=top_k)
    
    # Initialize the text splitter with overlap
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  # Max chunk size
        chunk_overlap=200  # Overlap between chunks
    )

    all_chunks = []
    
    # Split each document into chunks with overlap
    for doc in docs_with_metadata:
        # Split the document text into chunks
        chunks = text_splitter.split_text(doc.page_content)
        
        # Add the chunks to the list
        for chunk in chunks:
            all_chunks.append(chunk)
    
    #added comment
    return all_chunks