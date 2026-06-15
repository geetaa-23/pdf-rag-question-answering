# PDF RAG Question Answering System

## Overview

This project is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions based on their content. The system extracts text from PDFs, creates semantic embeddings, retrieves relevant information, and generates context-aware answers.

## Features

* Upload PDF documents through a Streamlit interface
* Extract text from PDF files
* Split documents into manageable chunks
* Generate embeddings using Sentence Transformers
* Store embeddings using FAISS vector database
* Perform semantic similarity search
* Generate answers using a Large Language Model (LLM)
* Display source chunks used for answer generation

## Tech Stack

* Python
* Streamlit
* PyMuPDF (fitz)
* Sentence Transformers
* FAISS
* NumPy
* Ollama / Gemini API
* Hugging Face Models

## Project Structure

```text
pdf-rag/
│
├── app.py
├── parser.py
├── chunker.py
├── embedder.py
├── vector_store.py
├── retriever.py
├── generator.py
├── test_retrieval.py
├── test_rag.py
├── requirements.txt
└── README.md
```

## Workflow

1. Upload a PDF document.
2. Extract text from the PDF.
3. Split the text into chunks.
4. Generate embeddings for each chunk.
5. Store embeddings in a FAISS index.
6. Convert the user question into an embedding.
7. Retrieve the most relevant chunks.
8. Generate an answer using the retrieved context.
9. Display the answer and source chunks.

## Installation

Clone the repository:

```bash
git clone https://github.com/geetaa-23/pdf-rag-question-answering.git
cd pdf-rag-question-answering
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the local URL provided in the terminal (usually http://localhost:8501).

## Example Questions

* What are the objectives of Python Programming?
* What are the advantages of Python?
* Explain functions in Python.
* What are Python modules?
* What topics are covered in the syllabus?

## Learning Outcomes

Through this project, the following concepts were explored:

* Retrieval-Augmented Generation (RAG)
* Semantic Search using Embeddings
* Vector Databases with FAISS
* PDF Text Extraction
* LLM-based Question Answering
* Streamlit Application Development

## Future Improvements

* Support multiple PDF uploads
* Chat history functionality
* Source highlighting
* Better chunking strategies
* Cloud deployment support
* Hybrid search (keyword + semantic search)

## Author

Geeta

## License

This project is developed for learning and educational purposes.
