from typing import List

def chunk_document(documents: List[str], chunk_size: int = 300, overlap: int = 50) -> List[str]:
    """
    Splits documents into overlapping chunks of words.

    Args:
        documents (List[str]): List of document strings.
        chunk_size (int): Number of words per chunk.
        overlap (int): Number of overlapping words between chunks.

    Returns:
        List[str]: Flattened list of chunks from all documents.
    """
    all_chunks = []
    for doc in documents:
        words = doc.split()
        for i in range(0, len(words), chunk_size - overlap):
            chunk = words[i:i + chunk_size]
            if chunk:
                all_chunks.append(" ".join(chunk))
    return all_chunks
