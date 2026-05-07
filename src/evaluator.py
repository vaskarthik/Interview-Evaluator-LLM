import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
import re
from pathlib import Path

from src.langchain.chains import evaluation_chain
from src.langchain.retriever import retriever

# -------------------------------------------------------------------------
# RAG Configuration
# -------------------------------------------------------------------------

USE_RAG = True

# -------------------------------------------------------------------------
# Paths
# -------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
PROMPT_PATH = BASE_DIR / "prompts"

# -------------------------------------------------------------------------
# Load Prompt File
# -------------------------------------------------------------------------

def load_prompt(version: str) -> str:

    file_map = {
        "v1": "prompt_v1.txt",
        "v2": "prompt_v2.txt",
        "v3": "prompt_v3.txt"
    }

    with open(PROMPT_PATH / file_map[version], "r", encoding="utf-8") as f:
        return f.read()

# -------------------------------------------------------------------------
# Extract JSON Block From LLM Output
# -------------------------------------------------------------------------

def extract_json(text: str) -> str:

    matches = re.findall(r'\{[\s\S]*?\}', text, re.DOTALL)

    return matches[-1] if matches else text

# -------------------------------------------------------------------------
# Repair + Parse JSON
# -------------------------------------------------------------------------

def safe_json_load(text: str):

    try:
        return json.loads(text)

    except Exception:

        text = text.replace("\n", " ")

        # Fix common malformed JSON issues
        text = re.sub(r'"\s*yn\s*"', '": "', text)
        text = re.sub(r'"\s*:\s*"', '": "', text)
        text = re.sub(r',\s*}', '}', text)
        text = re.sub(r',\s*]', ']', text)

        try:
            return json.loads(text)

        except Exception:
            return None

# -------------------------------------------------------------------------
# Validate Expected Schema
# -------------------------------------------------------------------------

def is_valid_evaluation(parsed: dict) -> bool:

    required_keys = [
        "score",
        "strengths",
        "weaknesses",
        "improvements",
        "final_feedback"
    ]

    # Ensure all keys exist
    if not all(key in parsed for key in required_keys):
        return False

    # Validate score
    if not isinstance(parsed["score"], (int, float)):
        return False

    if not (0 <= parsed["score"] <= 10):
        return False

    # Validate final feedback
    if not isinstance(parsed["final_feedback"], str):
        return False

    if not parsed["final_feedback"].strip():
        return False

    return True

# -------------------------------------------------------------------------
# Main Evaluation Function
# -------------------------------------------------------------------------

def evaluate_answer(
    question: str,
    answer: str,
    prompt_version: str = "v3",
    temperature: float = 0.0
):

    base_prompt = load_prompt(prompt_version)

    # -------------------------------------------------------------
    # RAG Retrieval + Prompt Augmentation
    # -------------------------------------------------------------

    if USE_RAG:

        docs = retriever.invoke(question)

        retrieved_context = "\n".join(
            [doc.page_content for doc in docs]
        )

        final_prompt = f"""
{base_prompt}

RETRIEVED CONTEXT:
{retrieved_context}

INPUT:
Question: {question}

Candidate Answer:
{answer}
"""

    else:

        final_prompt = (
            base_prompt
            .replace("{question}", question)
            .replace("{answer}", answer)
        )

    # -------------------------------------------------------------
    # Debug Prompt
    # -------------------------------------------------------------

    print("\n==================================================")
    print("FINAL PROMPT SENT TO LLM")
    print("==================================================\n")

    print(final_prompt)

    print("\n==================================================\n")

    # -------------------------------------------------------------
    # LangChain Evaluation
    # -------------------------------------------------------------

    try:

        parsed = evaluation_chain.invoke({
            "final_prompt": final_prompt
        })

    except Exception as e:

        return {
            "error": "LangChain evaluation failed",
            "details": str(e)
        }

    # -------------------------------------------------------------
    # Validate Output
    # -------------------------------------------------------------

    if not parsed:

        return {
            "error": "Empty response from LangChain pipeline"
        }

    if not is_valid_evaluation(parsed):

        return {
            "error": "Invalid evaluation schema returned",
            "raw_output": parsed
        }

    # -------------------------------------------------------------
    # Normalize Score
    # -------------------------------------------------------------

    if isinstance(parsed.get("score"), str):

        try:

            parsed["score"] = int(
                parsed["score"].split("/")[0]
            )

        except Exception:

            parsed["score"] = None

    # -------------------------------------------------------------
    # Ensure Required Fields
    # -------------------------------------------------------------

    parsed.setdefault("strengths", [])
    parsed.setdefault("weaknesses", [])
    parsed.setdefault("improvements", [])
    parsed.setdefault("final_feedback", "")

    return parsed

# -------------------------------------------------------------------------
# Compare Prompt Versions
# -------------------------------------------------------------------------

def compare_prompt_versions(question: str, answer: str):

    results = {}

    for version in ["v1", "v2", "v3"]:

        results[version] = {

            "temp_0": evaluate_answer(
                question,
                answer,
                version,
                0.0
            ),

            "temp_07": evaluate_answer(
                question,
                answer,
                version,
                0.7
            )
        }

    return results