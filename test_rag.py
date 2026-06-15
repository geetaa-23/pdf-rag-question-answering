from parser import extract_text
from chunker import chunk_text
from embedder import create_embeddings, model
from vector_store import build_index
from retriever import search
from generator import generate_answer

# Load PDF
text = extract_text("sample.pdf")

# Create chunks
chunks = chunk_text(text)

# Create embeddings
embeddings = create_embeddings(chunks)

# Build FAISS index
index = build_index(embeddings)

# Question
question = "What are the objectives of Python Programming?"

# Convert question to embedding
query_embedding = model.encode(question)

# Retrieve relevant chunks
results = search(index, query_embedding)

# Combine retrieved chunks
context = "\n".join([chunks[i] for i in results])

# Generate answer
answer = generate_answer(question, context)

print("\nQUESTION:")
print(question)

print("\nANSWER:")
print(answer)