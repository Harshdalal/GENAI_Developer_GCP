
# gemini_utils.py

import google.generativeai as genai
import os

# Initialize Gemini
def initialize_gemini(api_key, model="models/gemini-1.5-flash-latest"):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model)

# Run prompt
def get_response(prompt, api_key, mode="code-generation"):
    model = initialize_gemini(api_key)

    task_prefix = {
        "code-generation": "Generate code for this task:\n",
        "bug-fixing": "Find and fix bugs in the following code:\n",
        "code-explanation": "Explain the following code in simple terms:\n"
    }

    full_prompt = task_prefix.get(mode, "") + prompt
    response = model.generate_content(full_prompt)
    return response.text
