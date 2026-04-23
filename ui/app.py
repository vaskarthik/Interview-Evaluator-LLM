import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.evaluator import evaluate_answer

st.title("Interview Evaluation Bot")

question = st.text_area("Interview Question")
answer = st.text_area("Candidate Answer")

prompt_version = st.selectbox("Prompt Version", ["v1", "v2", "v3"])
temperature = st.slider("Temperature", 0.0, 1.0, 0.0)

if st.button("Evaluate"):
    result = evaluate_answer(question, answer, prompt_version, temperature)

    if "error" in result:
        st.error(result["error"])
        st.text(result["raw_output"])
    else:
        st.success(f"Score: {result['score']}")
        st.write("### Strengths")
        st.write(result["strengths"])
        st.write("### Weaknesses")
        st.write(result["weaknesses"])
        st.write("### Improvements")
        st.write(result["improvements"])
        st.write("### Feedback")
        st.write(result["final_feedback"])