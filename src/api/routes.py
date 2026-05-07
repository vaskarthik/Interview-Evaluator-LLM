from fastapi import APIRouter

from src.api.schemas import (
    EvaluationRequest,
    EvaluationResponse
)

from src.api.services import evaluate_question


router = APIRouter()


@router.post(
    "/evaluate",
    response_model=EvaluationResponse
)
def evaluate(request: EvaluationRequest):

    result = evaluate_question(
        question=request.question,
        candidate_answer=request.candidate_answer
    )

    return result