import pickle
from pathlib import Path

import faiss

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings


# -------------------------------------------------------------------------
# Paths
# -------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent

VECTOR_DB_PATH = BASE_DIR / "vector_db"

INDEX_FILE = VECTOR_DB_PATH / "faiss_index.bin"
METADATA_FILE = VECTOR_DB_PATH / "metadata.pkl"


# -------------------------------------------------------------------------
# Embedding Model
# -------------------------------------------------------------------------

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# -------------------------------------------------------------------------
# Load FAISS Index
# -------------------------------------------------------------------------

index = faiss.read_index(str(INDEX_FILE))

with open(METADATA_FILE, "rb") as f:
    metadata = pickle.load(f)


# -------------------------------------------------------------------------
# Create LangChain FAISS Vector Store
# -------------------------------------------------------------------------

documents = [
    Document(page_content=text)
    for text in metadata
]

vector_store = FAISS.from_documents(
    documents,
    embedding_model
)

# Replace internally generated index with your saved index
vector_store.index = index


# -------------------------------------------------------------------------
# Create Retriever
# -------------------------------------------------------------------------

retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)