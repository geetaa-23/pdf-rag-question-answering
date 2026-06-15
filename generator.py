import ollama

def generate_answer(question, context):

    prompt = f"""
    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]