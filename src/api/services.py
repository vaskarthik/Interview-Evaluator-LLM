from src.evaluator import evaluate_answer


def evaluate_question(
    question: str,
    candidate_answer: str
):

    return evaluate_answer(
        question=question,
        answer=candidate_answer,
        prompt_version="v3",
        temperature=0.0
    )