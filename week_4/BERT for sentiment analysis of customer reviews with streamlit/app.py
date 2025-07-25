
import streamlit as st
from model.predict import predict_sentiment

st.set_page_config(page_title="BERT Sentiment Classifier", layout="centered")
st.title("🧠 BERT Sentiment Analysis")
st.write("Enter a customer review below to analyze its sentiment.")

user_input = st.text_area("✍️ Review Text", height=200)

if st.button("Analyze Sentiment"):
    with st.spinner("Analyzing using BERT..."):
        rating, confidence = predict_sentiment(user_input)
        st.success(f"🌟 Predicted Rating: {rating} stars")
        st.info(f"Confidence: {confidence:.2f}")
