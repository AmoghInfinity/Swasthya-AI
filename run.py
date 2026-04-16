from app.rag import load_documents, retrieve

load_documents()

queries = [
    "What should a diabetic patient eat?",
    "Foods to avoid in fatty liver",
    "High protein vegetarian foods"
]

for q in queries:
    print("\nQuery:", q)
    results = retrieve(q)

    for i, doc in enumerate(results["documents"][0]):
        print("\nResult", i+1)
        print(doc[:200])

from app.graph import graph

state = {
    "question": "What should I eat in fatty liver?",
    "messages": [],
    "eval_retries": 0
}

result = graph.invoke(state)

print("\nFinal Answer:\n")
print(result["answer"])