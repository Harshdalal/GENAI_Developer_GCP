
# app.py
import streamlit as st
from utils.translate import translate
from model.train import train_model
import os

st.set_page_config(page_title="English to Hindi Translator", layout="centered")

st.title("🧠 English to Hindi Translator (Transformer-based)")
input_text = st.text_input("Enter English sentence:", "")

if st.button("Translate"):
    if not os.path.exists("checkpoints/model.h5"):
        with st.spinner("Training the model, please wait..."):
            train_model()
    result = translate(input_text)
    st.success(f"🔁 Hindi Translation: {result}")
