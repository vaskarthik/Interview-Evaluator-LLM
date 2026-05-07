# AI Interview Evaluator — Dockerized FastAPI RAG Service

A production-style Generative AI backend service for evaluating technical interview answers using:

- Local LLM inference with Ollama
- Retrieval Augmented Generation (RAG)
- FAISS vector database
- Sentence-transformers embeddings
- FastAPI REST API
- Dockerized deployment
- Structured JSON evaluation responses

---

# Repository

[Interview-Evaluator-LLM Repository](https://github.com/vaskarthik/Interview-Evaluator-LLM/tree/exp/dockerized-ai-service?utm_source=chatgpt.com)

---

# Features

- Local LLM inference using Ollama (`phi3`, `llama3`)
- Semantic retrieval using FAISS
- Embedding generation using sentence-transformers
- Prompt augmentation using RAG
- Structured interview evaluation
- FastAPI REST API
- Swagger API documentation
- Dockerized AI backend deployment
- JSON validation and parsing
- Modular backend architecture

---

# Tech Stack

| Layer | Technology |
|---|---|
| Backend API | FastAPI |
| LLM Runtime | Ollama |
| LLM Models | phi3 / llama3 |
| Embeddings | sentence-transformers |
| Vector DB | FAISS |
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
RAG Pipeline
      ↓
Semantic Retriever
      ↓
FAISS Vector DB
      ↓
Retrieved Context
      ↓
Prompt Augmentation
      ↓
Ollama Local LLM
      ↓
Structured JSON Evaluation
```

---

# Repository Structure

```text
Interview-Evaluator-LLM/
│
├── data/
│   └── interview_knowledge.txt
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
│   ├── rag/
│   │   ├── embedder.py
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │   └── pipeline.py
│   │
│   ├── llm_client.py
│   └── evaluator.py
│
├── vector_db/
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

git checkout exp/dockerized-ai-service
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

# Run FastAPI Service (Without Docker)

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
  "candidate_answer": "Template is a reusable piece of code independent of datatype."
}
```

---

### Response

```json
{
  "score": 5,
  "strengths": [
    "Correct identification that templates are related to data types"
  ],
  "weaknesses": [
    "Lacked depth in explaining the concept"
  ],
  "improvements": [
    "Explain generic programming and template behavior."
  ],
  "final_feedback": "The answer is partially correct but lacks technical depth."
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
OLLAMA_URL = "http://host.docker.internal:11434/api/generate"
```

---

# Example Evaluation Flow

```text
Question
   ↓
Semantic Retrieval
   ↓
Relevant Context
   ↓
Prompt Augmentation
   ↓
LLM Evaluation
   ↓
Structured JSON Output
```

---

# Current Capabilities

- RAG-based answer evaluation
- Semantic search
- Local AI inference
- Dockerized deployment
- REST API serving
- Structured evaluation responses

---

# Future Improvements

- Streaming LLM responses
- LangChain integration
- Multi-agent evaluation
- Authentication and API keys
- Cloud deployment
- Kubernetes deployment
- Conversation memory
- Advanced prompt versioning

---

# 🔀 Branch Evolution

| Branch | Focus |
|---|---|
| `main` | Prompt Engineering + Gemini API |
| `exp/local-llm-ollama` | Local LLM Integration |
| `exp/rag-vector-db` | RAG + Vector Database |
| `exp/fastapi-ai-service` | FastAPI AI Backend Service |
| `exp/dockerized-ai-service` | Dockerized AI Deployment |

---

# 👨‍💻 Author

## Karthik Vas S

GenAI Engineer | LLM Systems | RAG Pipelines | AI Backend Engineering

GitHub:

[Karthik Vas GitHub](https://github.com/vaskarthik/Interview-Evaluator-LLM/tree/exp/dockerized-ai-service)

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
Dockerized Production-Style AI Service
```

with a strong focus on:
- understanding internal GenAI architecture
- backend AI engineering
- deployment workflows
- containerized inference systems
- modern RAG pipeline implementation
- production-oriented AI application design

---

# Learning Outcomes

This project demonstrates practical experience with:

- Generative AI backend engineering
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