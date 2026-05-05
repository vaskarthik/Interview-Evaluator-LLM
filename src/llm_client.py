from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# -------------------------------------------------------------------------
# NOTE:
# This project supports two modes of operation:
#
# 1. API Mode (Gemini) → Requires valid API key
# 2. Mock Mode        → Used to avoid API cost during development/testing
#
# By default, Mock Mode is enabled to ensure the project runs without
# external dependencies or cost.
#
# To enable real LLM evaluation:
# - Add GEMINI_API_KEY in .env file
# - Uncomment the API-based function below
# - Comment out the mock function
# -------------------------------------------------------------------------



# 🔹 API-based LLM call (Gemini)
# Uncomment this function to enable real LLM evaluation

'''
def call_llm(prompt: str, temperature: float = 0.0) -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config={
            "temperature": temperature,
            "max_output_tokens": 512
        }
    )

    return response.text
'''


# 🔹 Mock LLM response (default)
# Used for development/demo purposes to avoid API usage

def call_llm(prompt: str, temperature: float = 0.0) -> str:
    return """
    {
      "score": 7,
      "strengths": ["Correct basic concept"],
      "weaknesses": ["Lacks depth"],
      "improvements": ["Add examples"],
      "final_feedback": "Good but needs improvement"
    }
    """