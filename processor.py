from langchain_text_splitters import RecursiveCharacterTextSplitter

def make_chunks(text, meta):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    parts = splitter.split_text(text)
    return [{"text": p, "meta": meta} for p in parts]
