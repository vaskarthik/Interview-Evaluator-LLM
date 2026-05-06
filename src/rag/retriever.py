from src.rag.embedder import Embedder
from src.rag.vector_store import VectorStore


class Retriever:
    def __init__(self):
        print("🔄 Initializing retriever...")

        self.embedder = Embedder()

        self.vector_store = VectorStore()

        self.vector_store.load()

        print("✅ Retriever ready")

    def retrieve(self, query: str, top_k=3):
        """
        Retrieve top-k relevant chunks.
        """

        print(f"🔍 Searching for: {query}")

        query_embedding = self.embedder.encode(query)[0]

        results = self.vector_store.search(
            query_embedding,
            top_k=top_k
        )

        return results