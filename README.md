# AI Interview Evaluator — LangChain Orchestrated RAG Service

A production-style Generative AI backend service for evaluating technical interview answers using:

- Local LLM inference with Ollama
- Retrieval Augmented Generation (RAG)
- FAISS vector database
- LangChain orchestration
- Retriever abstraction
- FastAPI REST API
- Dockerized deployment
- Structured JSON evaluation responses

---

# Repository

[Interview-Evaluator-LLM Repository](https://github.com/vaskarthik/Interview-Evaluator-LLM/tree/exp/langchain-ai-orchestration?utm_source=chatgpt.com)

---

# Features

- Local LLM inference using Ollama (`phi3`, `llama3`)
- Semantic retrieval using FAISS
- Embedding generation using sentence-transformers
- Prompt augmentation using RAG
- LangChain PromptTemplate integration
- RunnableSequence orchestration (LCEL)
- Retriever abstraction using `.as_retriever()`
- Structured JSON parsing using JsonOutputParser
- FastAPI REST API
- Swagger API documentation
- Dockerized AI backend deployment
- Modular backend architecture

---

# Tech Stack

| Layer | Technology |
|---|---|
| Backend API | FastAPI |
| LLM Runtime | Ollama |
| LLM Models | phi3 / llama3 |
| Orchestration | LangChain |
| Embeddings | sentence-transformers |
| Vector DB | FAISS |
| Retrieval | LangChain Retriever |
| Deployment | Docker |
| API Docs | Swagger UI |
| Language | Python |

---

# Project Architecture

```text
Client Request
      ↓
FastAPI REST API
      ↓
LangChain Evaluation Chain
      ↓
Retriever Abstraction
      ↓
FAISS Vector DB
      ↓
Retrieved Context
      ↓
Prompt Augmentation
      ↓
PromptTemplate
      ↓
OllamaLLM
      ↓
JsonOutputParser
      ↓
Structured JSON Evaluation

# LangChain Concepts Implemented

## PromptTemplate

Reusable prompt abstraction for structured evaluation prompts.

---

## RunnableSequence (LCEL)

LangChain Expression Language orchestration:

```python
prompt | llm | parser
```

---

## Retriever Abstraction

Using:

```python
retriever.invoke(question)
```

instead of manual retrieval orchestration.

---

## JsonOutputParser

Structured JSON parsing and validation from LLM outputs.

---

# Repository Structure

```text
Interview-Evaluator-LLM/
│
├── data/
│   └── interview_knowledge.txt
│
├── prompts/
│   ├── prompt_v1.txt
│   ├── prompt_v2.txt
│   └── prompt_v3.txt
│
├── vector_db/
│   ├── faiss_index.bin
│   └── metadata.pkl
│
├── src/
│   ├── api/
│   │   ├── main.py
│   │   ├── routes.py
│   │   ├── schemas.py
│   │   └── services.py
│   │
│   ├── langchain/
│   │   ├── prompts.py
│   │   ├── llm.py
│   │   ├── output_parser.py
│   │   ├── chains.py
│   │   └── retriever.py
│   │
│   ├── rag/
│   │   ├── data_loader.py
│   │   ├── embedder.py
│   │   ├── vector_store.py
│   │   └── retriever.py
│   │
│   ├── evaluator.py
│   └── main.py
│
├── build_vector_db.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/vaskarthik/Interview-Evaluator-LLM.git

cd Interview-Evaluator-LLM

git checkout exp/langchain-ai-orchestration
```

---

# Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Download Ollama:

```text
https://ollama.com/download
```

---

# Pull Local LLM Model

```bash
ollama pull phi3
```

or

```bash
ollama pull llama3
```

---

# Start Ollama

```bash
ollama serve
```

---

# Build Vector Database

Generate embeddings and build FAISS vector DB:

```bash
python build_vector_db.py
```

This creates:

```text
vector_db/
├── faiss_index.bin
└── metadata.pkl
```

---

# Run FastAPI Service

```bash
uvicorn src.api.main:app --reload
```

---

# Swagger API Docs

Open:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoint

## POST `/evaluate`

### Request

```json
{
  "question": "What is a template?",
  "candidate_answer": "Template is reusable generic code independent of datatype."
}
```

---

### Response

```json
{
  "score": 7,
  "strengths": [
    "Correct understanding of generic reusable code"
  ],
  "weaknesses": [
    "Lacks deeper explanation of template instantiation"
  ],
  "improvements": [
    "Explain generic programming and template behavior in C++"
  ],
  "final_feedback": "The answer demonstrates basic understanding but requires more technical depth."
}
```

---

# Dockerized Deployment

## Build Docker Image

```bash
docker build -t interview-evaluator-ai .
```

---

## Run Docker Container

```bash
docker run -p 8000:8000 interview-evaluator-ai
```

---

# Important Docker Networking Note

Inside Docker, `localhost` refers to the container itself.

For Ollama communication from container → host machine:

```python
OLLAMA_BASE_URL = "http://host.docker.internal:11434"
```

---

# Example Evaluation Flow

```text
Question
   ↓
Retriever.invoke()
   ↓
Relevant Context
   ↓
Prompt Augmentation
   ↓
LangChain Chain
   ↓
OllamaLLM
   ↓
Structured JSON Output
```

---

# Current Capabilities

- RAG-based answer evaluation
- Semantic retrieval
- LangChain orchestration
- Retriever abstraction
- Local AI inference
- Dockerized deployment
- REST API serving
- Structured evaluation responses

---

# Future Improvements

- AI agents
- Tool calling
- Multi-agent evaluation
- LangGraph workflows
- Conversation memory
- Candidate progress tracking
- Streaming LLM responses
- Authentication and API keys
- Cloud deployment
- Kubernetes deployment

---

# 🔀 Branch Evolution

| Branch | Focus |
|---|---|
| `main` | Prompt Engineering + Gemini API |
| `exp/local-llm-ollama` | Local LLM Integration |
| `exp/rag-vector-db` | RAG + Vector Database |
| `exp/fastapi-ai-service` | FastAPI AI Backend Service |
| `exp/dockerized-ai-service` | Dockerized AI Deployment |
| `exp/langchain-ai-orchestration` | LangChain Orchestration + Retriever Abstraction |

---

# 👨‍💻 Author

## Karthik Vas S

GenAI Engineer | LLM Systems | RAG Pipelines | AI Backend Engineering

GitHub:

Karthik Vas GitHub Repository

---

# 📌 Key Takeaway

This project demonstrates the evolution from:

```text
Prompt Engineering
        ↓
Local LLM Systems
        ↓
Retrieval Augmented Generation (RAG)
        ↓
FastAPI AI Backend
        ↓
Dockerized AI Service
        ↓
LangChain Orchestration
        ↓
Retriever Abstraction
```

with a strong focus on:

- understanding internal GenAI architecture
- backend AI engineering
- orchestration systems
- retrieval abstraction
- deployment workflows
- containerized inference systems
- modern RAG pipeline implementation
- production-oriented AI application design

---

# Learning Outcomes

This project demonstrates practical experience with:

- Generative AI backend engineering
- LangChain orchestration
- LCEL (LangChain Expression Language)
- Retriever abstraction
- RAG architecture
- Semantic retrieval systems
- FastAPI backend development
- Docker containerization
- Local LLM inference
- AI deployment workflows
- Structured prompt engineering
- Vector database integration
- AI infrastructure debugging
- Container networking concepts