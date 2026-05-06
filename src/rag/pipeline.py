from src.rag.retriever import Retriever


class RAGPipeline:
    def __init__(self):
        print("🔄 Initializing RAG pipeline...")

        self.retriever = Retriever()

        print("✅ RAG pipeline ready")

    def build_context(self, query: str, top_k=3):
        """
        Retrieve relevant context chunks.
        """

        retrieved_chunks = self.retriever.retrieve(
            query,
            top_k=top_k
        )

        context = "\n".join(retrieved_chunks)

        return context

    def augment_prompt(
        self,
        question: str,
        answer: str,
        base_prompt: str
    ):
        """
        Inject retrieved context into prompt.
        """

        context = self.build_context(question)

        rag_prompt = f"""
Retrieved Context:
{context}

{base_prompt}

Question:
{question}

Candidate Answer:
{answer}
"""

        return rag_prompt