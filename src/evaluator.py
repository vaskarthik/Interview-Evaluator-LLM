import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
import re
from pathlib import Path
from src.llm_client import call_llm

BASE_DIR = Path(__file__).resolve().parent.parent
PROMPT_PATH = BASE_DIR / "prompts"


# ✅ Load prompt file
def load_prompt(version: str) -> str:
    file_map = {
        "v1": "prompt_v1.txt",
        "v2": "prompt_v2.txt",
        "v3": "prompt_v3.txt"
    }

    with open(PROMPT_PATH / file_map[version], "r", encoding="utf-8") as f:
        return f.read()


# ✅ Extract JSON block from LLM output
def extract_json(text: str) -> str:
    matches = re.findall(r'\{.*\}', text, re.DOTALL)
    return matches[-1] if matches else text


# ✅ Repair + parse JSON
def safe_json_load(text: str):
    try:
        return json.loads(text)
    except:
        text = text.replace("\n", " ")

        # Fix common issues
        text = re.sub(r'"\s*yn\s*"', '": "', text)
        text = re.sub(r'"\s*:\s*"', '": "', text)
        text = re.sub(r',\s*}', '}', text)
        text = re.sub(r',\s*]', ']', text)

        try:
            return json.loads(text)
        except:
            return None


# ✅ Validate expected schema
def is_valid_evaluation(parsed: dict) -> bool:
    required_keys = [
        "score",
        "strengths",
        "weaknesses",
        "improvements",
        "final_feedback"
    ]
    return all(key in parsed for key in required_keys)


# ✅ Retry logic
def call_with_retry(prompt: str, temperature: float, retries: int = 2):
    last_response = ""

    for attempt in range(retries):
        print(f"🔄 LLM attempt {attempt + 1}")

        response = call_llm(prompt, temperature)
        last_response = response

        print("📦 Raw LLM output:", response[:200])  # debug

        cleaned = extract_json(response)
        parsed = safe_json_load(cleaned)

        if parsed and is_valid_evaluation(parsed):
            print("✅ Valid evaluation JSON received")
            return parsed

        print("⚠️ Invalid or incomplete JSON, retrying...")

    return {
        "error": "Invalid JSON from LLM",
        "raw_output": last_response
    }


# ✅ Main evaluation function
def evaluate_answer(
    question: str,
    answer: str,
    prompt_version: str = "v1",
    temperature: float = 0.0
):
    base_prompt = load_prompt(prompt_version)

    final_prompt = (
        base_prompt
        .replace("{question}", question)
        .replace("{answer}", answer)
    )

    parsed = call_with_retry(final_prompt, temperature)

    if "error" in parsed:
        return parsed

    # Normalize score
    if isinstance(parsed.get("score"), str):
        try:
            parsed["score"] = int(parsed["score"].split("/")[0])
        except:
            parsed["score"] = None

    # Ensure fields
    parsed.setdefault("strengths", [])
    parsed.setdefault("weaknesses", [])
    parsed.setdefault("improvements", [])
    parsed.setdefault("final_feedback", "")

    return parsed


# ✅ Compare prompts
def compare_prompt_versions(question: str, answer: str):
    results = {}

    for version in ["v1", "v2", "v3"]:
        results[version] = {
            "temp_0": evaluate_answer(question, answer, version, 0.0),
            "temp_07": evaluate_answer(question, answer, version, 0.7)
        }

    return results