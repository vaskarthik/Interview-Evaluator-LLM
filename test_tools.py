from src.agents.tools import (
    retrieve_interview_knowledge,
    evaluate_candidate_answer,
)


# -------------------------------------------------------------------------
# Test Retrieval Tool
# -------------------------------------------------------------------------

print("\n=== Retrieval Tool ===\n")

retrieval_result = retrieve_interview_knowledge.invoke(
    "Explain Python multithreading"
)

print(retrieval_result)


# -------------------------------------------------------------------------
# Test Evaluation Tool
# -------------------------------------------------------------------------

print("\n=== Evaluation Tool ===\n")

evaluation_result = evaluate_candidate_answer.invoke(
    """
    Question: What is polymorphism in OOP?

    Answer: Polymorphism allows methods
    to behave differently based on objects.
    """
)

print(evaluation_result)