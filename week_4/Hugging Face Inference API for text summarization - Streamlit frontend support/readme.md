# real-world project using Hugging Face's facebook/bart-large-cnn model for text summarization, using the Hugging Face Inference API and a Streamlit frontend.

# ✅ Project Overview

Use Case: Summarize long content like articles, reports, or user-entered paragraphs.

Model: facebook/bart-large-cnn (abstractive summarization)

API: Hugging Face Inference API (no GPU/local model needed)

Frontend: Streamlit

# 📁 Folder Structure

hf_summarizer_app/

├── app.py                  # Streamlit frontend

├── utils.py                # Hugging Face API logic

├── requirements.txt

└── README.md

# 🔧 Step-by-Step Setup

✅ Step 1: Hugging Face API Key

Visit: https://huggingface.co/settings/tokens

Generate a Read Token

Copy it—you’ll need it in the app

✅ Step 2: Create the Project

✅ Step 3: Create requirements.txt

✅ Step 4: utils.py – Hugging Face Summarization Logic

✅ Step 5: app.py – Streamlit Frontend

# 🚀 How to Run the Project

Run the Streamlit App

CMD > streamlit run app.py

# ⚡ Optional Extensions

Add max summary length and min length options.

Upload .txt files to summarize.

Add export/download of summary.

