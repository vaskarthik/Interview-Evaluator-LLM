from src.agents.agent import agent_executor


response = agent_executor.run(
    question="What is polymorphism in OOP?",

    answer="""
Polymorphism allows methods
to behave differently based on objects.
"""
)


print("\n\n=== FINAL RESPONSE ===\n")

print(response)