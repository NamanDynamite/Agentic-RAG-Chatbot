Agentic RAG Chatbot with MCP

A multi-agent Retrieval-Augmented Generation (RAG) chatbot that uses a modular agent architecture based on Model Communication Protocol (MCP). 
Upload documents (PDF, DOCX, CSV, etc.), ask questions, and get contextual answers powered by Groq (LLaMA3) and FAISS-based retrieval using HuggingFace embeddings.


 Features
 Multi-agent architecture: Ingestion, Retrieval, LLM Response agents

 Supports multiple document formats: PDF, CSV, DOCX, PPTX, TXT, MD

 Embedding-based retrieval with FAISS

 Powered by sentence-transformers/all-MiniLM-L6-v2

 LLM response via Groq API using llama3-8b-8192

 Built with Streamlit UI



 Folder Structure

project/
│
├── agents/
│   ├── ingestion_agent.py
│   ├── retrieval_agent.py
│   ├── llm_response_agent.py
│   └── mcp.py
│
├── temp/             
├── app.py          
├── requirements.txt   
└── .env    

           
 Setup Instructions

1. Clone the Repository

git clone https://github.com/your-username/agentic-rag-chatbot.git
cd agentic-rag-chatbot

2. Create a Virtual Environment 

python -m venv venv
venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Add Environment Variables

Create a .env file in the root directory:

GROQ_API_KEY=groq_api_key_here
HF_TOKEN=huggingface_token_here

Run the App

streamlit run app.py
Once the app is running, open the browser at http://192.168.1.8:8501

How to Use

Upload one or more documents (pdf, docx, csv, pptx, txt, md)

Wait for "Files embedded and vector store is ready."

Ask a question related to the document.

Get a direct answer + source context.



Requirements

Python 3.9+

Streamlit

Langchain

Huggingface Hub

Langchain-Groq

FAISS



 Architecture Overview

User
 └── Streamlit UI
     ├── IngestionAgent ──> loads + splits documents
     ├── RetrievalAgent ──> embeds & retrieves chunks via FAISS
     └── LLMResponseAgent ──> generates answer using Groq (LLaMA3)
All communication follows the MCPMessage protocol for modularity and traceability.