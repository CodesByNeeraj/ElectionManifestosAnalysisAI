from secret_key import secret_key 
from openai import OpenAIError
from langchain.embeddings import OpenAIEmbeddings
from secret_key import secret_key

def evaluate_manifestos_with_overlap(query, db,llm,top_k):
    # Chunk documents with overlap to retain context
    embedding = OpenAIEmbeddings(openai_api_key=secret_key)
    query_embedding = embedding.embed_query(query)
    # Perform similarity search to retrieve the top k relevant chunks to the query
    docs_with_metadata = db.similarity_search_by_vector(query_embedding, k=top_k)
    
    #we will take the text of the top k document chunks and join them with double newlines
    #there will be a gap between the text retrived from each of the chunks
    #these will be used as context for the llm together with your prompt
    top_chunks = "\n\n".join([doc.page_content for doc in docs_with_metadata])

    prompt = f"""
    Limit your response to 15-20 sentences and answer in paragraphs.

    You are a political analyst helping to answer queries from the public regarding different political parties.
    Answer by taking reference from the manifestos.
    Be as unbiased as possible and be objective.

    Relevant Document Chunks:
    {top_chunks}

    User Query:
    {query}

    Instructions:
    - Thoroughly analyze the manifestos and relevant document chunks.
    - Provide a clean, unbiased, and factual response
    - Make it summarized and concise.
    - Only provide 15-20 max sentences of answer
    """

    # Step 3: Get the model response
    responses = []
    try:
        response = llm.invoke(prompt)
        responses.append(response.content)  # Use `.content` to get string
    except OpenAIError as e:
        print("Error:", e)
    
    # Combine all responses into one string 
    final_response = "\n".join(responses)
    return final_response
