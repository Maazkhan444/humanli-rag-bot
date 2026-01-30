import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

PERSIST_DIR = "chroma_db"

def get_db():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)

def add_chunks(db, chunks):
    texts = [c["text"] for c in chunks]
    metadatas = [c["meta"] for c in chunks]
    db.add_texts(texts, metadatas)
    db.persist()

def search(db, query, k=4):
    return db.similarity_search(query, k=k)
