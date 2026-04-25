import streamlit as st
from llm_engine import generate_response
from prompts import job_match_prompt
from rag_pipeline import find_best_match

st.set_page_config(page_title="AI Career Copilot", layout="centered")

st.title("🤖 AI Career Copilot")

st.write("Analyze your resume, match jobs, and get insights.")

# Input fields
resume = st.text_area("Paste your Resume")
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):

    if resume and job_desc:

        st.subheader("📊 Job Matching (LLM)")

        try:
            match_result = generate_response(job_match_prompt(resume, job_desc))
            st.write(match_result)
        except:
            st.error("LLM API not working (check API key or quota)")

        st.subheader("🧠 RAG Matching")

        rag_result = find_best_match(resume)
        st.write("Best Match Job:", rag_result["best_match"])
        st.write("Score:", rag_result["score"])

    else:
        st.warning("Please enter both Resume and Job Description")