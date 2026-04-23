import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def call_llm(prompt: str, temperature: float = 0.0) -> str:
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": temperature,
            "top_p": 1.0,
            "max_output_tokens": 512
        }
    )

    return response.text