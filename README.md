# GE2025 Singapore
# ElectionsAI helps people ask questions about political party manifestos and get clear and short answers. 

## Why Use It?
1. No need to read long, complicated manifestos.
2. Saves time and makes it easier to compare what different parties are saying.
3. Great for voters, researchers, or anyone who wants to make informed decisions.


## Features
1. Semantic Resume Search using OpenAI embeddings and ChromaDB

2. PDF Resume Loading from a local Resumes/ folder

3. GPT-powered Summary for each query

4. Vector Store with automatic rebuild support
 
5. Dev-friendly CLI to test job descriptions and see results instantly

## Powered By:
1. LangChain

2. Chroma

3. OpenAI API

4. PyPDFLoader for PDF handling and reading

## Steps to run the app 

## Clone the Repository
Open a terminal and run the following command to clone the repository to your local machine:

### cd "navigate to your preferred folder where you want to clone the project at"

### git clone https://github.com/CodesByNeeraj/resumefilterusingAI.git

## Run the setup.sh script
The setup.sh script will install all necessary dependencies and set up the environment.
Make sure the script has execution permissions. You can run:

### chmod +x setup.sh

Then, execute the script:

### ./setup.sh

## Run the Streamlit App
After running the setup.sh script, you can launch the Streamlit app with the following command:

### streamlit run main.py
This will start the Streamlit server, and you should see an output similar to:

Local URL: http://localhost:8501
Network URL: http://<your-local-ip>:8501
