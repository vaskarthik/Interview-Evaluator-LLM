from langchain_core.prompts import PromptTemplate


evaluation_prompt = PromptTemplate(
    input_variables=[
        "question",
        "answer",
    ],

    template="""
You are an expert technical interviewer.

Evaluate the candidate answer.

Question:
{question}

Candidate Answer:
{answer}

Provide evaluation in this format:

Score: <score>/10

Technical Feedback:
<feedback>

Suggested Improvement:
<improvement>
"""
)