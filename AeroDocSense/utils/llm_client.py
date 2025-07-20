import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from configs import settings


HF_TOKEN = settings.HF_TOKEN

# Initialize Hugging Face chat client
client = InferenceClient(
    provider="featherless-ai",
    api_key=HF_TOKEN,
)

def generate_answer_from_chunks(query: str, context_chunks: list, max_tokens=512) -> str:
    """
    Generate an answer from LLM using context chunks and user query.
    Uses HuggingFace InferenceClient for chat completion.
    """

    # Format context from chunks
    context = "\n\n".join([f"[Chunk {i+1}]\n{chunk['text']}" for i, chunk in enumerate(context_chunks)])

    # Build system prompt or user message
    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert assistant. Use the given document chunks to answer the question clearly and concisely."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Context:\n{context}\n\n"
                f"Question: {query}"
            ),
        },
    ]

    try:
        completion = client.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=messages,
            max_tokens=max_tokens,
            temperature=0.3,
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        print(f"[ERROR] LLM inference failed: {e}")
        return "Sorry, I couldn't generate a response at this time."