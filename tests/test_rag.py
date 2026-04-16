import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.rag import load_documents, retrieve

def test_rag():
    print("Loading documents...")
    load_documents()

    queries = [
        "diabetes diet",
        "fatty liver foods to avoid",
        "high protein vegetarian foods"
    ]

    for q in queries:
        print("\nQuery:", q)
        results = retrieve(q)

        docs = results["documents"][0]

        assert len(docs) > 0, "No documents retrieved"

        for i, doc in enumerate(docs):
            print(f"Result {i+1}: {doc[:100]}")

    print("\nRAG Test Passed")


if __name__ == "__main__":
    test_rag()