from sentence_transformers import SentenceTransformer


class Embedder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        print("🔄 Loading embedding model...")

        self.model = SentenceTransformer(model_name)

        print("✅ Embedding model loaded")

    def encode(self, texts):
        """
        Convert text(s) into embeddings.
        """

        if isinstance(texts, str):
            texts = [texts]

        embeddings = self.model.encode(texts)

        return embeddings