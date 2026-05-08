from src.agents.tools import (
    retrieve_interview_knowledge,
    evaluate_candidate_answer,
)


class InterviewAgent:

    def run(
        self,
        question: str,
        answer: str,
    ) -> str:

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

        return evaluation_result


# -------------------------------------------------------------------------
# Create Agent Instance
# -------------------------------------------------------------------------

agent_executor = InterviewAgent()