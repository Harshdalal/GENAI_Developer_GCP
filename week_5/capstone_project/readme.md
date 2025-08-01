# ✅ Project 1: Smart Legal Assistant — Summarize, Extract & Track Prompt Effectiveness

🔹 Problem Statement:

Build an LLM-based legal assistant that takes complex legal documents (contracts, agreements, case summaries) and:

> Summarizes the content

> Extracts named entities (parties, dates, jurisdictions)

> Provides plain English explanation

👉 The challenge is to optimize and track the effectiveness of different prompt templates (few-shot, zero-shot, CoT) using Langfuse or MLflow for prompt version tracking and evaluation metrics like:

> Summary coherence

> Named entity accuracy

> Token cost per prompt

🔹 Tech Stack & Instructions:

Model & API:

>Use gemini-1.5-flash or gemini-2.0-flash with your free API key

Frameworks:

>LangChain for prompt pipelines

>Langfuse or MLflow for tracking prompt performance

>Streamlit for frontend upload + UI interaction

>Docker for local containerization

>GCP Cloud Run / App Engine for cloud deployment

🔹 Functional Requirements:

>Upload PDF or text file via Streamlit

>Choose prompt version from dropdown (v1_few_shot, v2_zero_shot, v3_cot)

>See output: Summary, Entity list, Explanation

>Behind the scenes, every prompt execution is tracked (prompt string, latency, tokens used, accuracy score)

>Streamlit dashboard to compare prompt variants

# ✅ Project 2: Product Review Analyzer — Sentiment + Summary + Prompt Dashboard

🔹 Problem Statement:

Create an LLM-powered system that:

>Accepts user-generated product reviews (Amazon, Flipkart, etc.)

>Summarizes the key feedback

>Classifies sentiment

>Shows how different prompts affect accuracy, bias, and output length

👉 The challenge is to track prompt template versions and outputs across experiments using Langfuse or MLflow and show prompt performance in Streamlit.

🔹 Tech Stack & Instructions:

Model & API:

gemini-1.5-flash or gemini-2.0-flash via Gemini API

Framework:

>LangChain + LangGraph (optional for multi-step reasoning)

Prompt management via:

>Langfuse: prompt versions, traces, logs

>Or MLflow: custom tracking using log_param, log_metric, log_artifact

UI: Streamlit

Deployment:

>Use Docker to containerize app

>Deploy to GCP Cloud Run or App Engine

🔹 Functional Requirements:

>Text input field for review or CSV upload

>Choose task: “Summarize,” “Classify Sentiment,” or “Both”

>Choose prompt version (prompt_v1, prompt_v2_guided, etc.)

>Prompt version and response time logged

>Accuracy and coherence ratings saved by evaluator (Gemini auto-evaluator or manual)

>Display logs and metrics using Streamlit dashboard from Langfuse or MLflow





