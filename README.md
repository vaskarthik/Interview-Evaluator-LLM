# AI Interview Evaluator — Modular RAG + Workflow Orchestrated GenAI System

A production-style Generative AI application for evaluating technical interview answers using:

- Local LLM inference with Ollama
- Retrieval Augmented Generation (RAG)
- FAISS vector database
- LangChain orchestration
- Workflow-based agent architecture
- FastAPI backend service
- Streamlit frontend UI
- Structured evaluation output pipelines

---

# Overview

This project demonstrates the evolution from simple prompt engineering into a modular AI application architecture focused on:

- LLM application engineering
- RAG systems
- workflow orchestration
- retrieval abstraction
- local AI inference
- backend AI services
- structured AI outputs

The system evaluates candidate answers for technical interview questions by retrieving relevant knowledge context and generating grounded evaluation feedback using a local LLM.

---

# Key Features

- Local LLM inference using Ollama
- llama3 integration
- RAG-based evaluation pipeline
- Semantic retrieval using FAISS
- sentence-transformers embeddings
- LangChain PromptTemplate integration
- Reusable LangChain chains
- Tool abstraction using `@tool`
- Workflow orchestration layer
- Agent controller abstraction
- FastAPI REST API
- Streamlit UI
- Structured evaluation output parsing
- Modular backend architecture

---

# Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Backend API | FastAPI |
| Frontend UI | Streamlit |
| LLM Runtime | Ollama |
| LLM Model | llama3 |
| Orchestration | LangChain |
| Vector Database | FAISS |
| Embeddings | sentence-transformers |
| Retrieval | LangChain Retriever |
| AI Workflow | Manual Workflow Orchestration |
| Local Inference | Ollama |
| Deployment | Docker |

---

# System Architecture

```text
Client / Streamlit UI
        ↓
FastAPI Backend
        ↓
Agent Controller
        ↓
Workflow Layer
        ↓
Tools Layer
   ├── Retrieval Tool
   └── Evaluation Tool
        ↓
RAG Pipeline
        ↓
FAISS Vector Search
        ↓
Retrieved Context
        ↓
Prompt Augmentation
        ↓
llama3 (Ollama)
        ↓
Structured Evaluation Output
```

---

# Workflow Architecture

The project uses explicit workflow orchestration instead of black-box autonomous agents.

```text
Question
   ↓
Retriever Tool
   ↓
Retrieved Context
   ↓
Evaluation Tool
   ↓
LLM Evaluation
   ↓
Structured Response
```

This architecture improves:

- debuggability
- modularity
- orchestration visibility
- workflow extensibility
- future routing support

---

# Why Manual Workflow Orchestration?

During development, an important limitation was discovered:

- `phi3` in Ollama did not support reliable tool calling
- `llama3` also lacked stable native `.bind_tools()` support in the current Ollama runtime

Because of this, manual workflow orchestration was implemented instead of relying on framework-managed autonomous agents.

This resulted in a cleaner and more transparent execution architecture.

---

# LangChain Concepts Implemented

## PromptTemplate

Reusable structured prompts for evaluation workflows.

---

## Runnable Chains

Composable LangChain execution pipelines.

---

## Retriever Abstraction

Using:

```python
retriever.invoke(question)
```

instead of manual vector search handling.

---

## Tool Abstraction

Implemented reusable AI capabilities using:

```python
@tool
```

Examples:

- `retrieve_interview_knowledge`
- `evaluate_candidate_answer`

---

## Workflow Layer

Introduced explicit orchestration layer:

```text
Tools
   ↓
Workflows
   ↓
Agent Controller
```

to separate:
- orchestration
- execution
- business logic
- control flow

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
│   ├── agents/
│   │   ├── agent.py
│   │   ├── workflows.py
│   │   ├── tools.py
│   │   └── prompts.py
│   │
│   ├── langchain/
│   │   ├── llm.py
│   │   ├── chains.py
│   │   ├── retriever.py
│   │   ├── output_parser.py
│   │   └── prompts.py
│   │
│   ├── parsers/
│   │   └── evaluation_parser.py
│   │
│   ├── rag/
│   │   ├── data_loader.py
│   │   ├── embedder.py
│   │   ├── vector_store.py
│   │   └── retriever.py
│   │
│   ├── api/
│   │   ├── main.py
│   │   ├── routes.py
│   │   ├── services.py
│   │   └── schemas.py
│   │
│   └── ui/
│       └── streamlit_app.py
│
├── build_vector_db.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/vaskarthik/Interview-Evaluator-LLM.git

cd Interview-Evaluator-LLM
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

Download:

```text
https://ollama.com/download
```

---

# Pull Local Model

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

```bash
python build_vector_db.py
```

This generates:

```text
vector_db/
├── faiss_index.bin
└── metadata.pkl
```

---

# Run FastAPI Backend

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

# Run Streamlit UI

```bash
streamlit run src/ui/streamlit_app.py
```

---

# API Endpoint

## POST `/evaluate`

### Request

```json
{
  "question": "What is polymorphism in C++?",
  "candidate_answer": "Polymorphism allows objects to behave differently based on implementation."
}
```

---

### Example Response

```json
{
  "score": 6,
  "strengths": [
    "Basic understanding of polymorphism"
  ],
  "weaknesses": [
    "Lacks explanation of runtime polymorphism",
    "Missing examples of virtual functions"
  ],
  "improvements": [
    "Explain method overriding and virtual functions"
  ],
  "final_feedback": "The answer demonstrates partial understanding but lacks technical depth."
}
```

---

# Example Evaluation Flow

```text
Question
   ↓
Workflow Layer
   ↓
Retrieval Tool
   ↓
FAISS Similarity Search
   ↓
Retrieved Context
   ↓
Evaluation Tool
   ↓
Prompt Augmentation
   ↓
llama3
   ↓
Structured Evaluation Output
```

---

# Key Engineering Learnings

This project provided hands-on experience with:

- Local LLM inference systems
- RAG architecture
- semantic retrieval pipelines
- workflow orchestration
- retrieval abstraction
- LangChain execution chains
- AI backend engineering
- prompt contract design
- structured output validation
- parser layer design
- local model limitations
- FastAPI integration
- Streamlit frontend integration
- modular AI application architecture

---

# Important Practical Insights

## Local LLM Tool Calling Limitations

Current Ollama runtime showed limitations with:

- native tool calling
- `.bind_tools()`
- structured output consistency

This led to implementation of:
- manual orchestration
- explicit workflow execution
- parser validation layers

---

## Structured Output Reliability

Local models do not always reliably generate strict JSON.

This project explores:
- prompt contracts
- validation layers
- parser-based recovery
- deterministic prompting strategies

---

# Current Capabilities

- Technical interview evaluation
- RAG-based context grounding
- Semantic search
- Local LLM inference
- Workflow orchestration
- Structured evaluation responses
- API serving
- Streamlit UI integration
- Modular backend architecture

---

# Potential Future Enhancements

- Expanded interview knowledge base
- Improved retrieval quality
- Streaming responses
- Better structured output reliability
- Conversation memory
- Evaluation analytics dashboard

---

# Branch Evolution

| Branch | Focus |
|---|---|
| `main` | Initial Prompt Engineering |
| `exp/local-llm-ollama` | Local LLM Integration |
| `exp/rag-vector-db` | RAG + FAISS |
| `exp/fastapi-ai-service` | FastAPI Backend |
| `exp/dockerized-ai-service` | Dockerized Deployment |
| `exp/langchain-ai-orchestration` | LangChain Integration |
| `exp/tools-and-agents` | Workflow + Tools Architecture |

---

# Author

## Karthik Vas S

Software Engineer | GenAI Engineering | RAG Systems | AI Backend Engineering

---

# Key Takeaway

This project demonstrates the evolution from:

```text
Prompt Engineering
        ↓
Local LLM Systems
        ↓
Retrieval Augmented Generation (RAG)
        ↓
LangChain Orchestration
        ↓
Tool Abstraction
        ↓
Workflow-Based AI Architecture
        ↓
Structured AI Output Systems
```

with emphasis on:
- practical GenAI engineering
- modular AI system design
- orchestration workflows
- backend AI architecture
- retrieval systems
- local inference pipelines
- production-oriented AI application development