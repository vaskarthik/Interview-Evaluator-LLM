import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"  #"phi3"   # fast model for your system


def call_llm(prompt: str, temperature: float = 0.0) -> str:
    try:
        print("🔄 Calling local LLM...")

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "options": {
                    "temperature": temperature,
                    "num_predict": 300
                },
                "stream": False
            },
            timeout=60
        )

        result = response.json()

        # ✅ Validate response field
        if "response" not in result:
            return f'{{"error": "No response field", "raw": {result}}}'

        print("✅ LLM response received")

        return result["response"]

    except Exception as e:
        return f'{{"error": "LLM call failed", "details": "{str(e)}"}}'