from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="phi3",
    base_url="http://localhost:11434",
    temperature=0
)