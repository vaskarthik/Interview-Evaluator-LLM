# 🧠 Interview Evaluation Bot — Local RAG System

## 📌 Overview

This project is a fully local Retrieval Augmented Generation (RAG) based interview evaluation system built using:

* Local LLMs via Ollama
* Embedding models
* FAISS Vector Database
* Semantic Retrieval
* Prompt Engineering
* Structured JSON validation

The system evaluates candidate interview answers using retrieved contextual knowledge and grounded LLM reasoning.

This branch focuses on understanding and implementing the internal architecture of modern GenAI systems rather than relying only on hosted APIs.

---

# 🚀 Features

* ✅ Fully local inference using Ollama
* ✅ No paid API dependency
* ✅ RAG (Retrieval Augmented Generation)
* ✅ FAISS vector database
* ✅ Semantic search using embeddings
* ✅ Prompt augmentation with retrieved context
* ✅ Structured JSON output validation
* ✅ Retry + malformed JSON handling
* ✅ Prompt versioning (`v1`, `v2`, `v3`)
* ✅ Temperature experimentation
* ✅ CLI-based evaluation
* ✅ Streamlit UI support

---

# 🧱 Project Architecture

```text
User Question
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
```

---

# 📂 Project Structure

```text
Interview-Evaluator-LLM/
│
├── src/
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

* Zero-shot prompting
* Few-shot prompting
* Constraint-based prompting
* Structured output prompting

---

## 2. Retrieval Augmented Generation (RAG)

The system retrieves relevant contextual knowledge before calling the LLM.

Benefits:

* Reduced hallucinations
* Grounded responses
* Better evaluation quality

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

* JSON schema
* score ranges
* required fields
* empty outputs

This improves reliability of LLM responses.

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

## 3. Start Local Model

Recommended for most laptops:

```bash
ollama run phi3
```

This starts the local inference server:

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

# ▶️ Run Application

## CLI Mode

```bash
python src/main.py
```

---

## Streamlit UI

```bash
streamlit run ui/app.py
```

---

# 📊 Example RAG Flow

## User Question

```text
What is overfitting?
```

---

## Retrieved Context

```text
Overfitting occurs when a model memorizes training data.
```

---

## Final Prompt Sent to LLM

```text
Retrieved Context:
Overfitting occurs when a model memorizes training data.

<Question + Candidate Answer + Evaluation Prompt>
```

---

# 📌 Example Output

```json
{
  "score": 8,
  "strengths": [
    "Correct identification of the concept"
  ],
  "weaknesses": [
    "Answer lacks deeper explanation about model generalization"
  ],
  "improvements": [
    "Explain why overfitting negatively impacts unseen data performance",
    "Discuss techniques such as regularization and cross-validation"
  ],
  "final_feedback": "The answer demonstrates correct understanding of overfitting but would benefit from deeper explanation and practical mitigation techniques."
}
```

---

# 🧠 Engineering Learnings

This project explores important GenAI engineering concepts:

* Embedding generation
* Vector similarity search
* Retrieval pipelines
* Prompt grounding
* Hallucination reduction
* Structured output validation
* Retry mechanisms
* Local inference systems
* Context-aware evaluation

---

# ⚠️ Current Limitations

* Small knowledge base
* Basic line-based chunking
* Limited metadata support
* No reranking
* CPU inference latency on larger models

---

# 🔮 Future Improvements

* [ ] Chunk overlap strategy
* [ ] Token-aware chunking
* [ ] ChromaDB integration
* [ ] Hybrid retrieval (BM25 + semantic)
* [ ] Metadata filtering
* [ ] Streaming responses
* [ ] Evaluation benchmarking
* [ ] LangChain / LlamaIndex integration
* [ ] Multi-agent evaluation

---

# 🔀 Branch Evolution

| Branch                 | Focus                           |
| ---------------------- | ------------------------------- |
| `main`                 | Prompt Engineering + Gemini API |
| `exp/local-llm-ollama` | Local LLM integration           |
| `exp/rag-vector-db`    | RAG + Vector Database           |

---

# 👨‍💻 Author

Karthik Vas S

GenAI Engineer | LLM Systems | RAG Pipelines | AI Application Development

---

# 📌 Key Takeaway

This project demonstrates the evolution from:

```text
Prompt Engineering
        ↓
Local LLM Systems
        ↓
Retrieval Augmented Generation (RAG)
```

with a strong focus on understanding the internal architecture of modern GenAI systems.
