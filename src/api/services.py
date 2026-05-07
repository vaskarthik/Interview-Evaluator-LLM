from src.rag.pipeline import run_rag_pipeline


def evaluate_question(
    question: str,
    candidate_answer: str
):

    result = run_rag_pipeline(
        question=question,
        candidate_answer=candidate_answer
    )

    result["model"] = "phi3"

    return result