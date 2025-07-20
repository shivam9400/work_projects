import os
from typing import List, Dict
#from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import streamlit as st

def get_secret(key: str, default: str = None):
    # Try to load from Streamlit secrets first
    if key in st.secrets:
        return st.secrets[key]
    
    # Then try from environment
    return os.getenv(key, default)

#load_dotenv(dotenv_path="AeroDocSense/configs/.env")
HF_TOKEN = get_secret("HF_TOKEN")
MONGO_URI = get_secret("MONGO_URI")
MONGO_COLLECTION_NAME = get_secret("MONGO_COLLECTION", "embedded_chunks")

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

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