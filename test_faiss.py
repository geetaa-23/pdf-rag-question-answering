from parser import extract_text
from chunker import chunk_text
from embedder import create_embeddings
from vector_store import build_index

text = extract_text("sample.pdf")

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

index = build_index(embeddings)

print("Total vectors stored:")

print(index.ntotal)