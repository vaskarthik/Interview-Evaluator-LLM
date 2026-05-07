from fastapi import APIRouter

from src.api.schemas import (
    EvaluateRequest,
    EvaluateResponse
)

from src.api.services import evaluate_question


router = APIRouter()


@router.post(
    "/evaluate",
    response_model=EvaluateResponse
)
def evaluate(request: EvaluateRequest):

    result = evaluate_question(
        question=request.question,
        candidate_answer=request.candidate_answer
    )

    return result