import json
from pathlib import Path
from llm_client import call_llm

PROMPT_PATH = Path("prompts")

def load_prompt(version: str) -> str:
    file_map = {
        "v1": "prompt_v1.txt",
        "v2": "prompt_v2.txt",
        "v3": "prompt_v3.txt"
    }
    with open(PROMPT_PATH / file_map[version], "r") as f:
        return f.read()


def evaluate_answer(question: str, answer: str, prompt_version="v1", temperature=0.0):
    base_prompt = load_prompt(prompt_version)

    final_prompt = base_prompt.format(
        question=question,
        answer=answer
    )

    response = call_llm(final_prompt, temperature)

    try:
        parsed = json.loads(response)
    except Exception:
        parsed = {
            "error": "Invalid JSON from LLM",
            "raw_output": response
        }

    return parsed


def compare_prompt_versions(question, answer):
    results = {}

    for version in ["v1", "v2", "v3"]:
        results[version] = {
            "temp_0": evaluate_answer(question, answer, version, 0.0),
            "temp_07": evaluate_answer(question, answer, version, 0.7)
        }

    return results