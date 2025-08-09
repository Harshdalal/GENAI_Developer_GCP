# app.py

import streamlit as st
from main import graph  # 👈 Make sure main.py exposes `graph`
import os


st.set_page_config(page_title="LangGraph Agent", layout="centered")

st.title("🧠 LangGraph AI Agent")
st.markdown("This agent will decide whether to use a calculator or an LLM based on your query.")

# Input field
query = st.text_input("Ask me anything:", placeholder="e.g., What is 15 * 7?")

if st.button("Run Agent") and query:
    st.write("Running agent...")
    with st.spinner("Processing..."):
        input_state = {"query": query, "retry_count": 0}
        result = graph.invoke(input_state)

        st.success("Done!")

        # Final Answer
        st.subheader("✅ Final Answer")
        st.markdown(f"**{result.get('final_answer', 'No final answer found.')}**")

        # Intermediate Debug
        with st.expander("🪵 View Full State (Debug Info)"):
            st.json(result)
