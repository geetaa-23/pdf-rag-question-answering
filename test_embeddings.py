from parser import extract_text
from chunker import chunk_text
from embedder import create_embeddings

text = extract_text("sample.pdf")

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

print("Number of chunks:", len(chunks))

print("Embedding shape:")

print(embeddings.shape)