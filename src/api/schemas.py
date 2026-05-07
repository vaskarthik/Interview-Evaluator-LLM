from pydantic import BaseModel
from typing import List


class EvaluateRequest(BaseModel):

    question: str
    candidate_answer: str


class EvaluateResponse(BaseModel):

    score: int
    strengths: List[str]
    weaknesses: List[str]
    improvements: List[str]
    final_feedback: str
    model: str