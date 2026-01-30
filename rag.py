import streamlit as st
from groq import Groq

SYSTEM = """You must answer ONLY using the provided website text.
If the answer is not found, respond exactly:
The answer is not available on the provided website."""

def answer(docs, question):
    context = "\n\n".join([d.page_content for d in docs])
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    prompt = f"{SYSTEM}\n\nTEXT:\n{context}\n\nQUESTION:\n{question}"
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}],
        temperature=0
    )
    return res.choices[0].message.content
