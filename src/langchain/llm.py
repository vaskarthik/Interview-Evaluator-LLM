from langchain_ollama import ChatOllama


# -------------------------------------------------------------------------
# Local Ollama Chat Model
# -------------------------------------------------------------------------

llm = ChatOllama(
    model="llama3",
    temperature=0,
)