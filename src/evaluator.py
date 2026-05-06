import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
import re
from pathlib import Path

from src.llm_client import call_llm
from src.rag.pipeline import RAGPipeline

# -------------------------------------------------------------------------
# RAG Configuration
# -------------------------------------------------------------------------

USE_RAG = True

rag_pipeline = RAGPipeline()


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
# Retry Logic For LLM Calls
# -------------------------------------------------------------------------

def call_with_retry(
    prompt: str,
    temperature: float,
    retries: int = 2
):
    last_response = ""

    for attempt in range(retries):

        print(f"\n🔄 LLM attempt {attempt + 1}")

        response = call_llm(prompt, temperature)

        last_response = response

        print("\n📦 Raw LLM output:")
        print(response[:300])

        cleaned = extract_json(response)

        parsed = safe_json_load(cleaned)

        if parsed and is_valid_evaluation(parsed):
            print("\n✅ Valid evaluation JSON received")

            return parsed

        print("\n⚠️ Invalid or incomplete JSON, retrying...")

    return {
        "error": "Invalid JSON from LLM",
        "raw_output": last_response
    }


# -------------------------------------------------------------------------
# Main Evaluation Function
# -------------------------------------------------------------------------

def evaluate_answer(
    question: str,
    answer: str,
    prompt_version: str = "v1",
    temperature: float = 0.0
):

    base_prompt = load_prompt(prompt_version)

    # -------------------------------------------------------------
    # Base Prompt
    # -------------------------------------------------------------

    final_prompt = (
        base_prompt
        .replace("{question}", question)
        .replace("{answer}", answer)
    )

    # -------------------------------------------------------------
    # Apply RAG Augmentation
    # -------------------------------------------------------------

    if USE_RAG:

        final_prompt = rag_pipeline.augment_prompt(
            question,
            answer,
            final_prompt
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
    # LLM Call + Retry
    # -------------------------------------------------------------

    parsed = call_with_retry(final_prompt, temperature)

    if "error" in parsed:
        return parsed

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

