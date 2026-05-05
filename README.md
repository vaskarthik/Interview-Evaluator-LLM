# 🧠 Interview Evaluation Bot (LLM + Prompt Engineering)

## 📌 Overview

This project evaluates interview answers using Large Language Models (LLMs) with a focus on **prompt engineering techniques** and **controlled structured outputs**.

It demonstrates how different prompting strategies and decoding parameters influence LLM behavior in evaluation tasks.

---

## 🚀 Features

* ✅ Zero-shot vs Few-shot vs Optimized prompts
* ✅ Prompt versioning (`v1`, `v2`, `v3`)
* ✅ Temperature-based experimentation
* ✅ Structured JSON output enforcement
* ✅ CLI interface
* ✅ Streamlit UI

---

## 🧱 Project Structure

```
Interview-Evaluator-LLM/
│
├── src/
│   ├── main.py           # CLI interface
│   ├── evaluator.py      # Prompt execution & parsing
│   ├── llm_client.py     # Gemini API / Mock integration
│
├── ui/
│   └── app.py            # Streamlit UI
│
├── prompts/
│   ├── prompt_v1.txt     # Zero-shot
│   ├── prompt_v2.txt     # Few-shot
│   └── prompt_v3.txt     # Optimized prompt
│
├── .env                  # API key configuration
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Configure API Key (Optional)

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 🧠 LLM Execution Modes

This project supports two execution modes:

### 1. Mock Mode (Default)

* No API key required
* Returns predefined evaluation output
* Useful for development and demonstrations without API cost

---

### 2. API Mode (Gemini)

To enable real LLM evaluation:

1. Add your API key in `.env`:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

2. Update `src/llm_client.py`:

   * Uncomment the API-based `call_llm` function
   * Comment out the mock implementation

👉 This enables real-time evaluation using Gemini models.

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
LLM Call (Gemini API / Mock Mode)
   ↓
Response Generation
   ↓
JSON Extraction
   ↓
Parsed Evaluation Output
```

---

## 🔍 Prompt Engineering Insights

### 1. Zero-shot vs Few-shot

| Type           | Behavior                          |
| -------------- | --------------------------------- |
| Zero-shot      | Inconsistent, unstructured        |
| Few-shot       | Improved formatting and reasoning |
| Optimized (v3) | Most stable and deterministic     |

---

### 2. Why Prompt v3 Performs Best

* Enforces strict JSON output
* Adds explicit constraints
* Reduces hallucination
* Improves determinism

---

### 3. Hallucination Control Techniques

* Explicit formatting instructions
* Constrained output schema
* Avoid ambiguous prompts
* Lower temperature settings

---

### 4. Temperature Impact

| Temperature | Behavior                      |
| ----------- | ----------------------------- |
| 0.0         | Deterministic, stable         |
| 0.7         | Creative, but less consistent |

---

## 📊 Example Output

```json
{
  "score": 7,
  "strengths": ["Correct concept"],
  "weaknesses": ["Lacks depth"],
  "improvements": ["Add examples"],
  "final_feedback": "Good but needs improvement"
}
```

---

## 🔮 Future Improvements

* [ ] Add evaluation metrics & scoring calibration
* [ ] Integrate RAG (Retrieval Augmented Generation)
* [ ] Multi-LLM / multi-agent evaluation
* [ ] Structured schema validation (Pydantic)
* [ ] Performance benchmarking

---

## 🧠 Key Takeaways

* Prompt design directly impacts LLM output quality
* Structured outputs require strict constraints
* LLM responses are probabilistic and need control mechanisms
* Temperature tuning affects consistency vs creativity

---

## 🔀 Project Evolution

| Stage              | Branch                 | Focus                    |
| ------------------ | ---------------------- | ------------------------ |
| Prompt Engineering | `main`                 | API-based evaluation     |
| Local LLM          | `exp/local-llm-ollama` | Offline inference        |
| RAG (planned)      | `exp/rag-vector-db`    | Context-aware evaluation |

---

## 👨‍💻 Author

Karthik Vas S

GenAI Engineer | LLM Systems | Prompt Engineering | AI Application Development

---

## 📌 Note

👉 Default mode uses **mock responses (no API required)**
👉 Enable API mode for real LLM evaluation
👉 For local/offline LLM version, see: `exp/local-llm-ollama`
