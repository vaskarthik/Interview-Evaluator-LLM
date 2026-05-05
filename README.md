# 🧠 Interview Evaluation Bot — Local LLM (Ollama Version)

This branch demonstrates the transition from API-based LLM usage to a **fully local LLM system** using Ollama.

👉 No external API calls
👉 No cost
👉 Runs entirely on your machine

---

## 🚀 What’s New in This Branch

Compared to the `main` branch:

| Feature                | main (API)   | this branch (local)         |
| ---------------------- | ------------ | --------------------------- |
| LLM source             | Gemini API   | Ollama (local models)       |
| Cost                   | ❌ Paid usage | ✅ Free                      |
| Latency                | Fast         | Moderate (CPU-bound)        |
| Reliability            | High         | Requires retry + validation |
| Engineering complexity | Medium       | High                        |

---

## 🧠 Key Learnings

This branch focuses on **real-world LLM system challenges**:

* Handling **invalid JSON outputs**
* Managing **timeouts and slow inference**
* Implementing **retry mechanisms**
* Performing **schema validation**
* Balancing **model size vs performance**
* Understanding **local LLM limitations**

---

## 🧱 Project Structure

```
Interview-Evaluator-LLM/
│
├── src/
│   ├── main.py           # CLI interface
│   ├── evaluator.py      # Evaluation + retry + validation logic
│   ├── llm_client.py     # Ollama integration
│
├── ui/
│   └── app.py            # Streamlit UI
│
├── prompts/
│   ├── prompt_v1.txt
│   ├── prompt_v2.txt
│   └── prompt_v3.txt
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Install Ollama

👉 https://ollama.com

---

### 2. Pull models

```bash
ollama pull phi3
ollama pull llama3
```

---

### 3. Run a model (example)

```bash
ollama run phi3
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

### CLI Mode

```bash
python src/main.py
```

---

### Streamlit UI

```bash
streamlit run ui/app.py
```

---

## 🔄 System Flow

```
User Input
   ↓
Prompt Selection (v1 / v2 / v3)
   ↓
Local LLM Call (Ollama)
   ↓
Raw Output
   ↓
JSON Extraction
   ↓
JSON Repair
   ↓
Schema Validation
   ↓
Retry (if needed)
   ↓
Final Structured Output
```

---

## 🔍 Prompt Versions

| Version | Description                       |
| ------- | --------------------------------- |
| v1      | Basic instruction                 |
| v2      | Few-shot prompting                |
| v3      | Strict structured + deterministic |

👉 **v3 performs best with local LLMs**

---

## ⚠️ Known Challenges (Local LLM)

* ❗ Slow inference (CPU-bound)
* ❗ Occasional invalid JSON
* ❗ Truncated responses
* ❗ Timeout issues with large models

---

## 🛠️ Solutions Implemented

* ✅ Retry mechanism for failed outputs
* ✅ JSON extraction from noisy responses
* ✅ JSON repair logic for malformed outputs
* ✅ Schema validation for correctness
* ✅ Timeout handling
* ✅ Model switching support (`phi3` / `llama3`)

---

## ⚡ Model Comparison

| Model  | Speed   | Accuracy | Recommended Use  |
| ------ | ------- | -------- | ---------------- |
| phi3   | ⚡ Fast  | Medium   | Development      |
| llama3 | 🐢 Slow | High     | Final evaluation |

---

## 📊 Example Output

```json
{
  "score": 6,
  "strengths": ["Correct concept"],
  "weaknesses": ["Lacks depth"],
  "improvements": ["Add examples"],
  "final_feedback": "Good but needs improvement"
}
```

---

## 🔮 Next Steps (Future Work)

* [ ] Vector Database (FAISS / Chroma)
* [ ] RAG (Retrieval Augmented Generation)
* [ ] Multi-LLM evaluation (generator + critic)
* [ ] Latency benchmarking
* [ ] Confidence scoring

---

## 🧠 Key Takeaway

> Moving from API-based LLMs to local models introduces real engineering challenges like reliability, latency, and output validation.

This branch focuses on solving those problems.

---

## 👨‍💻 Author

Karthik V S  
GenAI Engineer | LLM Systems | Prompt Engineering | AI Application Development

---

## 📌 Note

👉 For API-based version, check the `main` branch
👉 This branch focuses on **local LLM experimentation**
