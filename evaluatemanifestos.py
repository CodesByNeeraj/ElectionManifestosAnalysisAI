from openai import OpenAI
from chunkdocs import chunk_documents_with_overlap
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI #wrapper that lets you use chatgpt like models
#A wrapper function is a function in a software library or a computer program whose main purpose is to call a second subroutine or a system call with little or no additional computation. 
from secret_key import secret_key # Add `openai_api_key=...` if needed
#temperature = 0 to return more deterministic and focused responses (good for consistent evaluations
from openai import OpenAIError
from langchain.embeddings import OpenAIEmbeddings
from secret_key import secret_key

def evaluate_manifestos_with_overlap(query, db,llm,top_k):
    # Chunk documents with overlap to retain context
    embedding = OpenAIEmbeddings(openai_api_key=secret_key)
    query_embedding = embedding.embed_query(query)
    # Perform similarity search to retrieve the top relevant chunks
    docs_with_metadata = db.similarity_search_by_vector(query_embedding, k=top_k)  # k is the number of chunks to retrieve
    top_chunks = "\n\n".join([doc.page_content for doc in docs_with_metadata])

    #responses = []
    #relevant_chunks = [result.page_content for result in results]  # Extract the most relevant chunks
    prompt = f"""
    Limit your response to exactly 5 sentences.

    You are a political analyst helping to answer queries from the public regarding the manifestos of different political parties.
    Answer based solely on the manifestos.

    Relevant Document Chunks:
    {top_chunks}

    User Query:
    {query}

    Instructions:
    - Thoroughly analyze the manifestos.
    - Provide a clean, unbiased, and factual response based on the manifestos.
    - Make it summarized and concise.
    - Only provide 5 sentence answer
    """

    # Step 3: Get the model response
    responses = []
    try:
        response = llm.invoke(prompt)
        responses.append(response.content)  # Use `.content` to get string
    except OpenAIError as e:
        print("Error:", e)
    
    # Combine all responses into one string (if needed)
    final_response = "\n".join(responses)
    return final_response