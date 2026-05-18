from src.agents.workflows import (
    interview_evaluation_workflow,
)


def main():

    question = "Explain encapsulation"

    answer = """
    Encapsulation is wrapping data and methods
    together into a single unit.
    """

    result = interview_evaluation_workflow(
        question=question,
        answer=answer,
    )

    print("\n========== WORKFLOW RESULT ==========\n")

    print(result)


if __name__ == "__main__":
    main()