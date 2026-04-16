from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
from data.documents import documents

model = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.Client(Settings(
    persist_directory="./chroma_db"
))

collection = client.get_or_create_collection(name="health_kb")


def load_documents():
    if collection.count() > 0:
        print("Documents already loaded")
        return

    texts = [doc["text"] for doc in documents]
    ids = [doc["id"] for doc in documents]
    metadatas = [{"topic": doc["topic"]} for doc in documents]

    embeddings = model.encode(texts).tolist()

    collection.add(
        documents=texts,
        embeddings=embeddings,
        ids=ids,
        metadatas=metadatas
    )

    print("Documents loaded into Chroma")


def retrieve(query):
    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    return results