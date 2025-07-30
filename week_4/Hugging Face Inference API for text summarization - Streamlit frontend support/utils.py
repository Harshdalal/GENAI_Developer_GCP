import requests
import os

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

#HF_TOKEN = os.getenv("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")  # Read from environment variable for security

#headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query(payload):
    token = os.getenv("HF_TOKEN")
    if not token:
        return {"error": "No Hugging Face token provided."}

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json().get("error", "Request failed")}

def summarize_text(text):
    result = query({"inputs": text})
    if isinstance(result, dict) and "error" in result:
        return result
    return result[0]["summary_text"]
