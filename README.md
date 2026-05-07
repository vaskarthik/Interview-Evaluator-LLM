# 🧠 Interview Evaluation Bot — FastAPI RAG AI Service

## 📌 Overview

This project is a fully local Retrieval Augmented Generation (RAG) based interview evaluation system exposed through a production-style FastAPI backend service.

Built using:

* Local LLMs via Ollama
* FastAPI REST APIs
* Embedding models
* FAISS Vector Database
* Semantic Retrieval
* Prompt Engineering
* Structured JSON validation

The system evaluates candidate interview answers using retrieved contextual knowledge and grounded LLM reasoning.

This branch focuses on transforming the earlier local RAG prototype into a deployable AI backend architecture using FastAPI and modular service-oriented design.

---

# 🚀 Features

* ✅ Fully local inference using Ollama
* ✅ No paid API dependency
* ✅ FastAPI backend service
* ✅ REST API endpoint (`/evaluate`)
* ✅ Swagger/OpenAPI documentation
* ✅ RAG (Retrieval Augmented Generation)
* ✅ FAISS vector database
* ✅ Semantic search using embeddings
* ✅ Prompt augmentation with retrieved context
* ✅ Structured JSON evaluation output
* ✅ Prompt versioning + score calibration
* ✅ Startup optimized pipeline initialization
* ✅ Schema validated API responses
* ✅ Retry-safe malformed JSON fallback
* ✅ CLI + Streamlit compatibility retained

---

# 🧱 Project Architecture

```text
Client Request
      ↓
FastAPI REST API
      ↓
RAG Pipeline
      ↓
Embedding Generation
      ↓
FAISS Vector Search
      ↓
Top-K Context Retrieval
      ↓
Prompt Augmentation
      ↓
Local LLM (Ollama)
      ↓
Structured Evaluation Output
      ↓
JSON API Response
```

---

# 📂 Project Structure

```text
Interview-Evaluator-LLM/
│
├── src/
│   ├── api/
│   │   ├── main.py
│   │   ├── routes.py
│   │   ├── schemas.py
│   │   └── services.py
│   │
│   ├── main.py
│   ├── evaluator.py
│   ├── llm_client.py
│   │
│   ├── rag/
│   │   ├── embedder.py
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │   ├── pipeline.py
│   │   └── data_loader.py
│
├── data/
│   ├── interview_knowledge.txt
│   └── chunks.json
│
├── vector_db/
│
├── prompts/
│   ├── prompt_v1.txt
│   ├── prompt_v2.txt
│   └── prompt_v3.txt
│
├── ui/
│   └── app.py
│
├── build_vector_db.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Tech Stack

| Component       | Technology            |
| --------------- | --------------------- |
| Backend API     | FastAPI               |
| API Server      | Uvicorn               |
| Local LLM       | Ollama                |
| Models          | phi3 / llama3         |
| Embeddings      | sentence-transformers |
| Embedding Model | all-MiniLM-L6-v2      |
| Vector Database | FAISS                 |
| UI              | Streamlit             |
| Language        | Python                |

---

# 🧠 Core GenAI Concepts Implemented

## 1. Prompt Engineering

Implemented:

* Constraint-based prompting
* Structured JSON prompting
* Evaluation prompt versioning
* Score calibration rules
* Deterministic output control

Example:

```text
- Score must be between 0 and 10
- If answer is partially correct, score should be between 4 and 7
```

---

## 2. Retrieval Augmented Generation (RAG)

The system retrieves relevant contextual knowledge before calling the LLM.

Benefits:

* Reduced hallucinations
* Grounded responses
* Better evaluation quality
* Context-aware scoring

---

## 3. Embeddings

Text is converted into dense semantic vectors using:

```text
all-MiniLM-L6-v2
```

Example:

```text
"What is overfitting?"
      ↓
[0.12, -0.45, 0.88, ...]
```

---

## 4. Semantic Retrieval

FAISS retrieves the most semantically relevant knowledge chunks using vector similarity search.

---

## 5. Structured Output Validation

The system validates:

* JSON parsing
* score ranges
* required fields
* malformed outputs

This improves reliability of LLM responses.

---

## 6. AI Backend Engineering

Implemented:

* FastAPI service architecture
* REST API endpoints
* Swagger/OpenAPI docs
* Pydantic request/response schemas
* Startup optimized pipeline loading
* Modular service layer design

---

# 🚀 Setup Instructions

## 1. Install Ollama

Download and install:

👉 https://ollama.com

---

## 2. Pull Local Models

```bash
ollama pull phi3
ollama pull llama3
```

---

## 3. Verify Ollama Running

```bash
ollama list
```

Local inference server:

```text
http://localhost:11434
```

---

# 📦 Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

# 🧠 Build Vector Database

Before running evaluation, generate embeddings and build the FAISS vector DB:

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

# ▶️ Run FastAPI Service

```bash
uvicorn src.api.main:app --reload
```

---

# 📘 Swagger API Docs

Open:

```text
http://127.0.0.1:8000/docs
```

---

# 📡 API Endpoint

## POST `/evaluate`

### Example Request

```json
{
  "question": "What is overfitting?",
  "candidate_answer": "Overfitting happens when model memorizes training data."
}
```

---

### Example Response

```json
{
  "score": 7,
  "strengths": [
    "Correctly identified memorization issue"
  ],
  "weaknesses": [
    "Did not explain generalization failure"
  ],
  "improvements": [
    "Mention unseen test data performance"
  ],
  "final_feedback": "Good basic understanding but answer lacks deeper explanation.",
  "model": "phi3"
}
```

---

# 📊 Example RAG Flow

## User Question

```text
What is a template in C++?
```

---

## Retrieved Context

```text
Templates in C++ allow generic programming.
```

---

## Final Prompt Sent to LLM

```text
Retrieved Context:
Templates in C++ allow generic programming.

<Question + Candidate Answer + Evaluation Prompt>
```

---

# 🧠 Engineering Learnings

This project explores important GenAI engineering concepts:

* FastAPI backend serving
* Embedding generation
* Vector similarity search
* Retrieval pipelines
* Prompt grounding
* Hallucination reduction
* Structured output validation
* Schema enforcement
* Local inference systems
* Context-aware evaluation
* AI backend architecture

---

# ⚠️ Current Limitations

* Small knowledge base
* Basic line-based chunking
* Limited metadata support
* No reranking
* No streaming responses yet
* CPU inference latency on larger models

---

# 🔮 Future Improvements

* [ ] Dockerization
* [ ] Docker Compose integration
* [ ] Streaming responses
* [ ] Async FastAPI inference
* [ ] Retry logic for malformed JSON
* [ ] Logging infrastructure
* [ ] LangChain / LlamaIndex integration
* [ ] Hybrid retrieval (BM25 + semantic)
* [ ] Multi-agent evaluation

---

# 🔀 Branch Evolution

| Branch                       | Focus                                |
| ---------------------------- | ------------------------------------ |
| `main`                       | Prompt Engineering + Gemini API      |
| `exp/local-llm-ollama`       | Local LLM integration                |
| `exp/rag-vector-db`          | RAG + Vector Database                |
| `exp/fastapi-ai-service`     | FastAPI AI Backend Service           |

---

# 👨‍💻 Author

Karthik Vas S

GenAI Engineer | LLM Systems | RAG Pipelines | AI Backend Engineering

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
Production-Style AI Backend Service
```

with a strong focus on understanding the internal architecture and deployment patterns of modern GenAI systems.