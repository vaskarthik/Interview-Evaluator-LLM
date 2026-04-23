# Interview Evaluation Bot (LLM + Prompt Engineering)

## Overview
This project evaluates interview answers using LLMs with controlled prompt engineering.

## Features
- Zero-shot vs Few-shot vs Optimized prompts
- Temperature control experiments
- CLI + Streamlit UI

## Setup

1. Install dependencies:
pip install -r requirements.txt

2. Add API key:
Create `.env` file:
GEMINI_API_KEY=your_key

## Run CLI
python src/main.py

## Run UI
streamlit run ui/app.py

---

## Learning Insights

### 1. Zero-shot vs Few-shot
- Zero-shot → inconsistent
- Few-shot → better structured outputs

### 2. Why Prompt v3 is Best
- Enforces JSON
- Reduces hallucination
- Adds constraints → more deterministic

### 3. Hallucination Control
- Explicit instructions
- Strict format
- Lower temperature

### 4. Temperature Impact
- 0 → deterministic
- 0.7 → creative but inconsistent scoring

---

## Future Improvements
- Add evaluation metrics
- Add RAG
- Add multi-agent evaluation