import streamlit as st
import google.generativeai as genai

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_answer(question, context):

    prompt = f"""
You are a helpful assistant.

Answer the question using ONLY the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text