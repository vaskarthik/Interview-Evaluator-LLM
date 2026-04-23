import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
import re
from pathlib import Path
from src.llm_client import call_llm

BASE_DIR = Path(__file__).resolve().parent.parent
PROMPT_PATH = BASE_DIR / "prompts"


def load_prompt(version: str) -> str:
    file_map = {
        "v1": "prompt_v1.txt",
        "v2": "prompt_v2.txt",
        "v3": "prompt_v3.txt"
    }

    with open(PROMPT_PATH / file_map[version], "r", encoding="utf-8") as f:
        return f.read()


# 🔍 Extract JSON safely from LLM output
def extract_json(text: str) -> str:
    match = re.search(r'\{[\s\S]*?\}', text)
    return match.group(0) if match else text


def evaluate_answer(
    question: str,
    answer: str,
    prompt_version: str = "v1",
    temperature: float = 0.0
):
    base_prompt = load_prompt(prompt_version)

    # ✅ Safe replacement (avoids .format() JSON issues)
    final_prompt = (
        base_prompt
        .replace("{question}", question)
        .replace("{answer}", answer)
    )

    response = call_llm(final_prompt, temperature)

    cleaned = extract_json(response)

    try:
        parsed = json.loads(cleaned)

        # ✅ Normalize score (handle "6/10" → 6)
        if isinstance(parsed.get("score"), str):
            try:
                parsed["score"] = int(parsed["score"].split("/")[0])
            except Exception:
                parsed["score"] = None

        # ✅ Ensure required fields exist
        parsed.setdefault("strengths", [])
        parsed.setdefault("weaknesses", [])
        parsed.setdefault("improvements", [])
        parsed.setdefault("final_feedback", "")

    except Exception:
        parsed = {
            "error": "Invalid JSON from LLM",
            "raw_output": response
        }

    return parsed


def compare_prompt_versions(question: str, answer: str):
    results = {}

    for version in ["v1", "v2", "v3"]:
        results[version] = {
            "temp_0": evaluate_answer(question, answer, version, 0.0),
            "temp_07": evaluate_answer(question, answer, version, 0.7)
        }

    return results