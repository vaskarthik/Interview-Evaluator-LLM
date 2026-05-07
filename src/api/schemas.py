from pydantic import BaseModel
from typing import List


class EvaluationRequest(BaseModel):

    question: str
    candidate_answer: str


class EvaluationResponse(BaseModel):

    score: int

    strengths: List[str]

    weaknesses: List[str]

    improvements: List[str]

    final_feedback: str