from src.agents.tools import (
    retrieve_interview_knowledge,
    evaluate_candidate_answer,
)


def interview_evaluation_workflow(
    question: str,
    answer: str,
):
    """
    Main interview evaluation workflow.
    """

    # -------------------------------------------------------------
    # Step 1 - Retrieve Context
    # -------------------------------------------------------------

    retrieval_query = question

    retrieved_context = retrieve_interview_knowledge.invoke(
        retrieval_query
    )

    # -------------------------------------------------------------
    # Step 2 - Build Evaluation Input
    # -------------------------------------------------------------

    evaluation_input = f"""
Question:
{question}

Answer:
{answer}

Additional Context:
{retrieved_context}
"""

    # -------------------------------------------------------------
    # Step 3 - Evaluate Answer
    # -------------------------------------------------------------

    evaluation_result = evaluate_candidate_answer.invoke(
        evaluation_input
    )

    # -------------------------------------------------------------
    # Step 4 - Return Structured Workflow Output
    # -------------------------------------------------------------

    return {
        "question": question,
        "answer": answer,
        "retrieved_context": retrieved_context,
        "evaluation": evaluation_result,
    }