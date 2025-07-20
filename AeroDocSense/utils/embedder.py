import os
from typing import List, Dict
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'configs', '.env')

#load_dotenv(dotenv_path="AeroDocSense\configs\.env")
load_dotenv(dotenv_path=dotenv_path)

HF_TOKEN = os.getenv("HF_API_TOKEN")
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

assert HF_TOKEN is not None

client = InferenceClient(
    model=MODEL_NAME,
    token=HF_TOKEN
)

def get_embedding(text: str) -> List[float]:
    """
    Get embedding using Hugging Face InferenceClient.
    """
    embedding = client.feature_extraction(text)
    return embedding.tolist()

def generate_embeddings(chunks: List[str]) -> List[Dict]:
    """
    Generate embeddings for a list of text chunks.

    Returns:
        List of dicts with 'text' and 'embedding'
    """
    embedded_chunks = []
    for text in chunks:
        vector = get_embedding(text)
        embedded_chunks.append({
            "text": text,
            "embedding": vector
        })
    return embedded_chunks

def generate_embedding_for_query(query: str) -> List[float]:
    """
    Generate embedding for a single query string (used in retrieval).
    Args:
        query (str): Search query.
    Returns:
        List[float]: Embedding vector.
    """
    return get_embedding(query)