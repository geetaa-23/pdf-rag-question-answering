import streamlit as st
from parser import extract_text
from chunker import chunk_text
from embedder import create_embeddings, model
from vector_store import build_index
from retriever import search
from generator import generate_answer

st.title("PDF RAG Question Answering")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    text = extract_text("temp.pdf")

    chunks = chunk_text(text)

    st.success(
        f"PDF loaded successfully! {len(chunks)} chunks created."
    )

    embeddings = create_embeddings(chunks)

    index = build_index(embeddings)

    question = st.text_input("Ask a question")

    if question:

        query_embedding = model.encode(question)

        results = search(
            index,
            query_embedding
        )

        context = "\n".join(
            [chunks[i] for i in results]
        )

        with st.spinner("Generating answer..."):
            answer = generate_answer(
                question,
                context
            )

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Sources")

        for i in results:
            st.write(f"Chunk {i}")
            st.text(chunks[i][:300])