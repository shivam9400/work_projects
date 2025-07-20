'''
1. Take a user query
2. Generate its embedding
3. Compare it with stored embeddings in MongoDB
4. Retrieve top-k most similar chunks (documents)
'''
import os
import numpy as np
from utils.embedder import generate_embedding_for_query
from utils.mongo_handler import MongoDBHandler
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import streamlit as st
from configs import settings


HF_TOKEN = settings.HF_TOKEN
MONGO_URI = settings.MONGO_DB_URI
MONGO_COLLECTION_NAME = settings.MONGO_COLLECTION

class DocumentRetrievalEngine:
    def __init__(self, top_k=5):
        self.mongo = MongoDBHandler(collection_name=MONGO_COLLECTION_NAME)
        self.top_k = top_k

    def search(self, query):
        # Step 1: Embed the query
        query_embedding = generate_embedding_for_query(query)

        # Step 2: Fetch all embedded chunks from MongoDB
        documents = self.mongo.find_all()
        if not documents:
            print("[ERROR] No documents found in database.")
            return []

        # Step 3: Extract embeddings and metadata
        chunk_texts = [doc["text"] for doc in documents]
        chunk_embeddings = np.array([doc["embedding"] for doc in documents], dtype=np.float32)

        # Step 4: Compute cosine similarities
        similarities = cosine_similarity([query_embedding], chunk_embeddings)[0]

        # Step 5: Sort and return top-k results
        top_indices = similarities.argsort()[::-1][:self.top_k]
        top_chunks = [{"text": chunk_texts[i], "score": float(similarities[i])} for i in top_indices]
        return top_chunks
