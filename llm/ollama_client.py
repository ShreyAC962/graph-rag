import ollama
from config import OLLAMA_MODEL

def generate_answer(context, question):
    prompt = f"""
    You are a knowledge graph reasoning assistant.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]