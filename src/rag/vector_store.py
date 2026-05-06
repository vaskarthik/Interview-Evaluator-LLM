import faiss
import numpy as np
import pickle
from pathlib import Path


VECTOR_DB_PATH = Path(__file__).resolve().parent.parent.parent / "vector_db"

INDEX_FILE = VECTOR_DB_PATH / "faiss_index.bin"
METADATA_FILE = VECTOR_DB_PATH / "metadata.pkl"


class VectorStore:
    def __init__(self, embedding_dimension=384):
        self.dimension = embedding_dimension

        # L2 distance index
        self.index = faiss.IndexFlatL2(self.dimension)

        self.metadata = []

    def add_embeddings(self, embeddings, chunks):
        """
        Store embeddings + corresponding text chunks.
        """

        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)

        self.metadata.extend(chunks)

    def search(self, query_embedding, top_k=3):
        """
        Search nearest vectors.
        """

        query_embedding = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query_embedding, top_k)

        results = []

        for idx in indices[0]:
            if idx < len(self.metadata):
                results.append(self.metadata[idx])

        return results

    def save(self):
        """
        Save FAISS index + metadata.
        """

        VECTOR_DB_PATH.mkdir(exist_ok=True)

        faiss.write_index(self.index, str(INDEX_FILE))

        with open(METADATA_FILE, "wb") as f:
            pickle.dump(self.metadata, f)

        print("✅ Vector DB saved")

    def load(self):
        """
        Load FAISS index + metadata.
        """

        self.index = faiss.read_index(str(INDEX_FILE))

        with open(METADATA_FILE, "rb") as f:
            self.metadata = pickle.load(f)

        print("✅ Vector DB loaded")