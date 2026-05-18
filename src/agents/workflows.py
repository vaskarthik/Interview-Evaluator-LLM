from src.agents.tools import (
    retrieve_interview_knowledge,
    evaluate_candidate_answer,
)

from src.parsers.evaluation_parser import (
    parse_evaluation_output,
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

    raw_evaluation = evaluate_candidate_answer.invoke(
        evaluation_input
    )

    print("\n========== RAW LLM OUTPUT ==========\n")
    print(raw_evaluation)

    parsed_evaluation = parse_evaluation_output(
        raw_evaluation
    )

    # -------------------------------------------------------------
    # Step 4 - Return Structured Workflow Output
    # -------------------------------------------------------------

    return {
        "question": question,
        "answer": answer,
        "retrieved_context": retrieved_context,
        "evaluation": parsed_evaluation,
    }