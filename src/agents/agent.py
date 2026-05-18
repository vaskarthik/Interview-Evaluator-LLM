from src.agents.workflows import (
    interview_evaluation_workflow,
)


class InterviewAgent:

    def run(
        self,
        question: str,
        answer: str,
    ):

        return interview_evaluation_workflow(
            question=question,
            answer=answer,
        )


# -------------------------------------------------------------------------
# Create Agent Instance
# -------------------------------------------------------------------------

agent_executor = InterviewAgent()