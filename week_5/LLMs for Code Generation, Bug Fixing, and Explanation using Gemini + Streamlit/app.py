
import streamlit as st
from gemini_utils import get_response

st.set_page_config(page_title="LLM Code Assistant", layout="wide")
st.title("💻 LLM-Powered Code Assistant (Gemini 1.5 Flash)")

with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input("🔑 Gemini API Key", type="password")
    task_mode = st.selectbox(
        "🧠 Task Type",
        ["code-generation", "bug-fixing", "code-explanation"]
    )

if api_key:
    st.subheader("📝 Enter your prompt or code")
    user_input = st.text_area("Write your instruction or code here", height=300)

    if st.button("🚀 Run"):
        with st.spinner("Running Gemini 1.5 Flash..."):
            result = get_response(user_input, api_key, mode=task_mode)
            st.markdown("### 🧾 Response")
            st.code(result, language="python" if task_mode != "code-explanation" else "text")
else:
    st.warning("Please enter your Gemini API Key to proceed.")
