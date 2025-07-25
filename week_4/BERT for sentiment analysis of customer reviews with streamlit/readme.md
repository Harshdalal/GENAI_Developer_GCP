# Real-world use case project using BERT for sentiment analysis of customer reviews

# ✅ Project Overview

Use Case: Sentiment Analysis on Product Reviews

Model: Pretrained BERT (bert-base-uncased) from HuggingFace

Frontend: Streamlit

Dataset: IMDB movie reviews (or upload your own)

# 📁 Folder Structure

bert_sentiment_app/

├── app.py                      # Streamlit frontend

├── model/

│   ├── __init__.py

│   ├── train.py                # Fine-tune BERT (optional)

│   └── predict.py              # Inference logic

├── data/

│   └── sample_reviews.csv      # Sample dataset

├── requirements.txt

└── README.md

# Step-by-Step Setup

✅ Step 1: Create the Folder

CMD > mkdir bert_sentiment_app

CMD > cd bert_sentiment_app

✅ Step 2: Create requirements.txt

pip install -r requirements.txt


# 🚀 How to Run the Project

Run the Streamlit App

CMD > streamlit run app.py

# 🔁 Optional Enhancements

You can extend the project by:

Adding a training script using IMDB dataset (train.py)

Visualizing word-level attention using bertviz

Uploading CSVs for batch prediction

Logging results with timestamp in a log.csv




