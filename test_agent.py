from src.agents.agent import agent_executor


def main():

    question = "What is polymorphism in C++?"

    answer = """
    Polymorphism allows objects to behave differently
    based on the method implementation.
    """

    result = agent_executor.run(
        question=question,
        answer=answer,
    )

    print("\n========== FINAL RESULT ==========\n")

    print(result)


if __name__ == "__main__":
    main()