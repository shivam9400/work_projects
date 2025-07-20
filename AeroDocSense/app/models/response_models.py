from pydantic import BaseModel
from typing import List

class Chunk(BaseModel):
    text: str
    score: float

class RAGResponse(BaseModel):
    query: str
    chunks: List[Chunk]
