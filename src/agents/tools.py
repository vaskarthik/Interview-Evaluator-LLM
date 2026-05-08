from langchain.tools import tool

from src.langchain.retriever import retriever
from src.langchain.chains import evaluation_chain


# -------------------------------------------------------------------------
# Retrieval Tool
# -------------------------------------------------------------------------

@tool
def retrieve_interview_knowledge(query: str) -> str:
    """
    Retrieve interview-related technical knowledge
    from the vector database.
    """

    docs = retriever.invoke(query)

    formatted_docs = []

    for doc in docs:
        formatted_docs.append(doc.page_content)

    return "\n\n".join(formatted_docs)


# -------------------------------------------------------------------------
# Evaluation Tool
# -------------------------------------------------------------------------

@tool
def evaluate_candidate_answer(input_text: str) -> str:
    """
    Evaluate a candidate interview answer.

    Input format:

    Question: <question>
    Answer: <answer>
    """

    try:

        sections = input_text.split("Answer:")

        question = sections[0].replace(
            "Question:",
            ""
        ).strip()

        answer = sections[1].strip()

        result = evaluation_chain.invoke(
            {
                "question": question,
                "answer": answer,
            }
        )

        return str(result)

    except Exception as e:

        return f"Evaluation error: {str(e)}"