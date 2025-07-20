from app.search import DocumentRetrievalEngine
from utils.llm_client import generate_answer_from_chunks

# Initialize retrieval engine with desired top-k
retriever = DocumentRetrievalEngine(top_k=5)

def answer_query(query: str) -> str:
    """
    Given a user query:
    - Retrieve top-k relevant document chunks
    - Generate LLM-based answer using RAG
    """
    print(f"[INFO] Searching relevant chunks for query: '{query}'")
    relevant_chunks = retriever.search(query)

    if not relevant_chunks:
        return "No relevant information found in the document corpus."

    print("[INFO] Generating answer using LLM...")
    response = generate_answer_from_chunks(query, relevant_chunks)

    return response
