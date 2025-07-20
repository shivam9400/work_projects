from app.search import DocumentRetrievalEngine
from app.generate import answer_query

user_query = "what is aerospace hydraulic system?"

engine = DocumentRetrievalEngine(top_k=5)
results = engine.search(user_query)

for idx, res in enumerate(results, 1):
    print(f"\nResult #{idx} [Score: {res['score']:.4f}]\n{res['text']}")

print("\nSearch completed. Now generating answer...")

answer = answer_query(user_query)
print("\nFinal Answer:\n", answer)