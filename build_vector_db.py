from src.rag.data_loader import load_knowledge_base, chunk_text
from src.rag.embedder import Embedder
from src.rag.vector_store import VectorStore


print("🔄 Loading knowledge base...")

text = load_knowledge_base()

chunks = chunk_text(text)

print(f"✅ Loaded {len(chunks)} chunks")

print("🔄 Generating embeddings...")

embedder = Embedder()

embeddings = embedder.encode(chunks)

print("✅ Embeddings generated")

print("🔄 Creating vector store...")

vector_store = VectorStore()

vector_store.add_embeddings(embeddings, chunks)

vector_store.save()

print("✅ Vector DB creation complete")