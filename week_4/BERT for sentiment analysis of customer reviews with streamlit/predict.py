
# model/predict.py
import torch
from transformers import BertTokenizer, BertForSequenceClassification
import os

MODEL_NAME = 'nlptown/bert-base-multilingual-uncased-sentiment'

# Load model and tokenizer once
tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)
model = BertForSequenceClassification.from_pretrained(MODEL_NAME)

def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    confidence, prediction = torch.max(probs, dim=1)
    sentiment = int(prediction.item()) + 1  # 1 to 5 star
    return sentiment, confidence.item()
