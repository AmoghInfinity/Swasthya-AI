import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.graph import graph
from app.rag import load_documents


def test_graph():
    print("Loading KB...")
    load_documents()

    queries = [
        "What should I eat in diabetes?",
        "Foods to avoid in fatty liver",
        "High protein vegetarian diet"
    ]

    for q in queries:
        print("\nQuery:", q)

        state = {
            "question": q,
            "messages": [],
            "eval_retries": 0
        }

        result = graph.invoke(state)

        answer = result["answer"]

        print("Answer:", answer[:200])

        assert answer is not None
        assert len(answer) > 10
        assert "I don't know" not in answer  # IMPORTANT

    print("\nGraph Test Passed")


if __name__ == "__main__":
    test_graph()