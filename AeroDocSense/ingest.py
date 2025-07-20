'''
The script will perform the following tasks:
- Load documents from data/sample_docs/
- Chunk them using chunker.py
- Generate embeddings via embedder.py
- Store chunks + vectors in MongoDB using mongo_handler.py
'''
import os
import fitz
from utils.chunker import chunk_document
from utils.embedder import generate_embeddings
from utils.mongo_handler import MongoDBHandler


DOCUMENTS_PATH = "AeroDocSense\data"

def extract_text_from_pdf(file_path):
    """Extract text content from a PDF using PyMuPDF."""
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def main():
    documents = []
    for filename in os.listdir(DOCUMENTS_PATH):
        file_path = os.path.join(DOCUMENTS_PATH, filename)
        if filename.endswith(".pdf"):
            try:
                text = extract_text_from_pdf(file_path)
                documents.append(text)
            except Exception as e:
                print(f"[ERROR] Could not read PDF {filename}: {e}")

        elif filename.endswith(".txt"):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    documents.append(f.read())
            except Exception as e:
                print(f"[ERROR] Could not read TXT {filename}: {e}")
        else:
            print(f"[SKIPPED] Unsupported file format: {filename}")
    print(f"Loaded {len(documents)} raw documents")

    # Chunk documents
    chunks = chunk_document(documents, chunk_size=30, overlap=5)
    print(f"Generated {len(chunks)} chunks")

    # Generate embeddings
    embedded_chunks = generate_embeddings(chunks)
    print("Embeddings generated for all chunks")

    # Store in MongoDB
    MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "embedded_chunks")
    mongo = MongoDBHandler(collection_name=MONGO_COLLECTION)
    mongo.insert_many(embedded_chunks)
    print("Chunks stored in MongoDB successfully")

if __name__ == "__main__":
    main()