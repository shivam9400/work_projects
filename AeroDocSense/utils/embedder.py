import os
from typing import List, Dict
from huggingface_hub import InferenceClient
import streamlit as st
from configs import settings


HF_TOKEN = settings.HF_TOKEN
MONGO_URI = settings.MONGO_DB_URI
MONGO_COLLECTION_NAME = settings.MONGO_COLLECTION

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