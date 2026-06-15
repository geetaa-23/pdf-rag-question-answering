from parser import extract_text
from chunker import chunk_text
from embedder import create_embeddings, model
from vector_store import build_index
from retriever import search

text = extract_text("sample.pdf")

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

index = build_index(embeddings)

question = "What are the objectives of Python Programming?"

query_embedding = model.encode(question)

results = search(index, query_embedding)

print("Top Results:\n")

for i in results:
    print("=" * 50)
    print(chunks[i][:500])