import streamlit as st
from crawler import scrape_site
from processor import make_chunks
from embeddings import get_db, add_chunks, search
from rag import answer

st.set_page_config(page_title="Website Chatbot", layout="centered")
st.title("Website Chatbot")

if "db_ready" not in st.session_state:
    st.session_state.db_ready = False

url = st.text_input("Enter a website URL")

if st.button("Index Website") and url:
    with st.spinner("Scraping and indexing..."):
        text, meta = scrape_site(url)
        chunks = make_chunks(text, meta)
        db = get_db()
        add_chunks(db, chunks)
        st.session_state.db_ready = True
    st.success("Website indexed")

question = st.text_input("Ask a question")

if question and st.session_state.db_ready:
    with st.spinner("Searching..."):
        docs = search(get_db(), question, k=4)
        reply = answer(docs, question)
        st.write(reply)
