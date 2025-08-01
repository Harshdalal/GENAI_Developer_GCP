
import streamlit as st
from graph import build_graph
from dotenv import load_dotenv
import os

load_dotenv()
graph = build_graph()

st.set_page_config(page_title="Finance Analyzer AI", layout="centered")
st.title("💼 Agentic Finance Analyzer")

st.markdown("Paste a financial article, report, or news item. Two AI agents will run in parallel:")

st.markdown("- 📈 Trend Analysis")
st.markdown("- ⚠️ Risk Assessment")

user_input = st.text_area("📝 Paste your financial text here", height=200)

if st.button("Analyze"):
    with st.spinner("Analyzing with Gemini Agents..."):
        result = graph.invoke({"input": user_input})
        st.success("✅ Analysis Complete")
        st.subheader("📊 Final Report")
        st.write(result["report"])
