# Humanli Website Chatbot (RAG)

## What it does
Indexes a website and answers questions strictly from that content using embeddings and a grounded LLM.

## Stack
- Streamlit UI
- Website crawler with BeautifulSoup
- Chunking with LangChain
- Embeddings: all-MiniLM-L6-v2
- Vector DB: Chroma (persistent)
- LLM: Llama-3 via Groq API (free tier)

## Security
API keys are stored in Streamlit Secrets and never committed to GitHub.

## Run locally
1. Create `.streamlit/secrets.toml`
   GROQ_API_KEY="your_key"
2. `pip install -r requirements.txt`
3. `streamlit run app.py`

## Deploy
Push to GitHub.  
On Streamlit Cloud add secret `GROQ_API_KEY`.  
Deploy app.py.
