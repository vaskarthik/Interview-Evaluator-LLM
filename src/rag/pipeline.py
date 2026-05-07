import json

from src.rag.retriever import Retriever
from src.llm_client import call_llm


class RAGPipeline:

    def __init__(self):

        print("🔄 Initializing RAG pipeline...")

        self.retriever = Retriever()

        print("✅ RAG pipeline ready")

    def build_context(self, query: str, top_k=1):
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
        candidate_answer: str,
        context: str
    ):
        """
        Build final RAG evaluation prompt.
        """

        rag_prompt = f"""
You are a strict technical interviewer.

Use the retrieved context to evaluate the candidate answer.

RETRIEVED CONTEXT:
{context}

TASK:
Evaluate the candidate answer based on:
- correctness
- depth
- clarity
- completeness

STRICT RULES:
- Output MUST be valid JSON
- Do NOT add any explanation outside JSON
- Score must be between 0 and 10
- If answer is partially correct, score should be between 4 and 7
- If answer is mostly correct but lacks depth, score should be between 6 and 8
- Weak answers should include weaknesses
- final_feedback must NOT be empty

FORMAT:
{{
  "score": integer between 0 and 10,
  "strengths": [],
  "weaknesses": [],
  "improvements": [],
  "final_feedback": ""
}}

Return ONLY JSON.

INPUT:
Question: {question}

Candidate Answer:
{candidate_answer}
"""

        return rag_prompt


# ---------------------------------------------------
# Initialize pipeline ONCE during application startup
# ---------------------------------------------------

pipeline_instance = RAGPipeline()


def run_rag_pipeline(
    question: str,
    candidate_answer: str
):

    # Retrieve semantic context
    context = pipeline_instance.build_context(question)

    # Build augmented prompt
    prompt = pipeline_instance.augment_prompt(
        question=question,
        candidate_answer=candidate_answer,
        context=context
    )

    print("📄 Final Prompt Sent To LLM:\n")
    print(prompt)

    # Generate LLM response
    llm_response = call_llm(prompt)

    print("🧠 Raw LLM Response:\n")
    print(llm_response)

    # Parse JSON response
    try:

        parsed_response = json.loads(llm_response)

        return parsed_response

    except Exception as e:

        print("❌ JSON parsing failed")
        print(e)

        return {
            "score": 0,
            "strengths": [],
            "weaknesses": [
                "LLM failed to return valid JSON."
            ],
            "improvements": [
                "Retry generation with stricter formatting."
            ],
            "final_feedback": "Failed to parse LLM response."
        }