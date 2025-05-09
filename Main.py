import streamlit as st
import streamlit.components.v1 as components
from evaluatemanifestos import evaluate_manifestos_with_overlap
from createvectordatabase import create_db
from langchain.chat_models import ChatOpenAI
from secret_key import secret_key
# Initialize OpenAI model
llm = ChatOpenAI(openai_api_key=secret_key, temperature=0)

def main():
  st.title("Singapore Elections Map - 2025")

  #iframe is what displays the interactive map 
  iframe_code = """ 
  <iframe
    id="responsive-iframe"
    src="https://elections.data.gov.sg/en/map?isScrollable=true&primaryColor=%236253E8&view=Winning%20margin&lang=en&year=2025&constituenciesView=all"
    frameborder="0"
    scrolling="no"
    width="100%"
    height="642px"
  >
  </iframe>
  """

  height = st.slider("Adjust map height", 400, 1200, 680)
  components.html(iframe_code, height=height)
  
  query = st.text_input("Ask a question about the manifestos:")
  
  if query: 
    
  # Load the full manifesto data (no similarity search in this case)
    db = create_db()
    
    # Initialize the LLM (OpenAI model) for response generation
    llm = ChatOpenAI(openai_api_key=secret_key, temperature=0)
    
    # Process the query and evaluate manifestos by chunking
    answer = evaluate_manifestos_with_overlap(query, db, llm,3)
    st.write(answer)
   
if __name__ == "__main__":
    main()
   
  
