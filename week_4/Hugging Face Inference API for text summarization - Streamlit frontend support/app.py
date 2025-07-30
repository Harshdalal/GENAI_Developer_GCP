
# app.py
import streamlit as st
from utils import summarize_text
import os

st.set_page_config(page_title="📝 Text Summarizer", layout="centered")
st.title("📚 Text Summarizer using Hugging Face BART")
st.markdown("Model: `facebook/bart-large-cnn` via Hugging Face Inference API")

hf_token = st.text_input("🔐 Enter your Hugging Face API Token", type="password")

default_text = """The Apollo 11 mission was the first manned mission to land on the Moon. 
It was launched on July 16, 1969, and carried astronauts Neil Armstrong, Buzz Aldrin, 
and Michael Collins. On July 20, Armstrong and Aldrin became the first humans to walk on the Moon, 
while Collins orbited above. The mission marked a major milestone in space exploration and 
fulfilled President John F. Kennedy’s goal of landing a man on the Moon and returning him safely to Earth."""

input_text = st.text_area("✍️ Enter text to summarize", value=default_text, height=300)

if st.button("Summarize"):
    if not hf_token:
        st.error("Please enter your Hugging Face token.")
    else:
        os.environ["HF_TOKEN"] = hf_token
        with st.spinner("Summarizing..."):
            summary = summarize_text(input_text)
        if isinstance(summary, dict) and "error" in summary:
            st.error(f"❌ Error: {summary['error']}")
        else:
            st.subheader("📌 Summary")
            st.success(summary)
