from fastapi import FastAPI
from app.search import DocumentRetrievalEngine
from app.generate import answer_query
from app.models.request_models import QueryRequest
from app.models.response_models import RAGResponse
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="AeroDocSense/configs/.env")
hf_token = os.getenv("HF_API_TOKEN")

app = FastAPI(
    title="AeroDocSense - RAG API",
    description="Search and generate answers from aerospace documents (specific to Hydraulic Systems)",
    version="1.0"
)

retriever = DocumentRetrievalEngine(top_k=5)

@app.post("/search", response_model=RAGResponse)
def search_chunks(request: QueryRequest):
    chunks = retriever.search(request.query)
    return RAGResponse(query=request.query, chunks=chunks)

@app.post("/generate", response_model=dict)
def rag_generate(request: QueryRequest):
    chunks = retriever.search(request.query)
    answer = answer_query(request.query)
    return {"answer": answer}
