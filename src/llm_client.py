from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

''' def call_llm(prompt: str, temperature: float = 0.0) -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config={
            "temperature": temperature,
            "max_output_tokens": 512
        }
    )

    return response.text  '''

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
