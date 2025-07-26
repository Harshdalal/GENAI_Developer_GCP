import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import google.generativeai as genai
import uuid
import concurrent.futures
import time
from langfuse import get_client

# --------------------------
# 🔧 Configurations
# --------------------------
genai.configure(api_key="AIzaSyCff1JjsKqnqYRm9JiJOWQ8WXV9ukzU614")  # Replace with your actual Gemini API key

AVAILABLE_MODELS = {
    "Gemini 1.5 Flash": "models/gemini-1.5-flash",
    "Gemini 1.5 Pro": "models/gemini-1.5-pro"
}

langfuse = get_client()  # Global singleton

# --------------------------
# 🎯 Prompt Evaluation Function
# --------------------------
def evaluate_prompt_quality(prompt: str, response: str, model_name: str) -> str:
    eval_prompt = f"""Rate the **clarity, coherence, completeness, and relevance** of this AI response on a scale of 1–10 and explain briefly:

**Prompt**: {prompt}
**Response**: {response}

Give result as:
Score: <score>
Reason: <explanation>"""

    model = genai.GenerativeModel(model_name)
    result = model.generate_content(eval_prompt)
    return result.text.strip()

# --------------------------
# 🧠 Run Prompt Logic (Background Thread)
# --------------------------
def run_prompt_task(prompt_text: str, trace_name: str, selected_model: str):
    with langfuse.start_as_current_span(
        name="gemini-span",
        input={"prompt": prompt_text},
    ) as span:
        span.update_trace(
            name=trace_name,
            user_id="test-user",
            session_id=str(uuid.uuid4()),
        )

        model = genai.GenerativeModel(selected_model)
        response_stream = model.generate_content(prompt_text, stream=True)

        output = ""
        for chunk in response_stream:
            if chunk.text:
                output += chunk.text

        span.output = output
        span.end()

        quality = evaluate_prompt_quality(prompt_text, output, selected_model)

    return {
        "Prompt": prompt_text,
        "Model": selected_model.split("/")[-1],
        "Output": output,
        "Output Length": len(output),
        "Quality Score": quality,
        "Trace ID": span.trace_id
    }

# --------------------------
# 🌐 Streamlit UI
# --------------------------
st.set_page_config(page_title="Gemini Scorecard Streamlit", layout="wide")
st.title("🔮 Gemini Prompt Scorecard App")
st.markdown("Run multiple Gemini prompts in parallel with quality evaluation and model selection.")

# Model selection
model_label = st.selectbox("🧠 Select Gemini Model", list(AVAILABLE_MODELS.keys()))
selected_model = AVAILABLE_MODELS[model_label]

# Prompt inputs
st.subheader("📨 Enter Your Prompts")
num_prompts = st.slider("Number of Prompts", 1, 4, 2)
default_prompts = [
    "Explain quantum computing in simple terms.",
    "Summarize the latest AI trends in 100 words.",
    "What is the difference between fusion and fission?",
    "Describe black holes to a 5-year-old."
]

user_prompts = []
for i in range(num_prompts):
    user_input = st.text_input(f"Prompt {i+1}", value=default_prompts[i] if i < len(default_prompts) else "")
    user_prompts.append(user_input)

# Run prompts
if st.button("🚀 Run Prompts"):
    st.write("🔄 Running Gemini and evaluating...")

    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(run_prompt_task, prompt, f"trace-{i}", selected_model)
            for i, prompt in enumerate(user_prompts)
        ]

        for future in futures:
            results.append(future.result())

    df = pd.DataFrame(results)
    df.index = [f"Prompt {i+1}" for i in range(len(df))]

    st.dataframe(df[["Prompt", "Model", "Output Length", "Quality Score", "Trace ID"]])

    # Plot comparison
    fig = make_subplots(rows=1, cols=2, subplot_titles=["📝 Output Length", "📈 Quality Score"])
    fig.add_trace(go.Bar(x=df.index, y=df["Output Length"], name="Length", marker_color="blue"), row=1, col=1)

    # Parse score from "Score: <n>"
    scores = []
    for q in df["Quality Score"]:
        try:
            score_line = [line for line in q.splitlines() if line.lower().startswith("score")][0]
            score_val = int(score_line.split(":")[1].strip())
        except Exception:
            score_val = 0
        scores.append(score_val)

    fig.add_trace(go.Bar(x=df.index, y=scores, name="Score", marker_color="orange"), row=1, col=2)
    fig.update_layout(title="📊 Prompt Output Metrics", height=400, width=1000)
    st.plotly_chart(fig, use_container_width=True)

    # Show individual outputs
    st.subheader("📄 Full Gemini Outputs")
    for i, row in df.iterrows():
        st.markdown(f"### {i} — Model: {row['Model']}")
        st.info(row["Output"])
        st.markdown(f"**Quality:** {row['Quality Score']}")
