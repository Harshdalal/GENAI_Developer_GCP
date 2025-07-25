
import os
import streamlit as st
from PIL import Image
import google.generativeai as genai
import speech_recognition as sr
import tempfile

# Configure Gemini API
GOOGLE_API_KEY = "AIzaSyA2JAHidciNxDbzC-R25DqRFzuQWq6mzIw"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


# Function: Process one image with prompt
def process_image_with_prompt(image_file, prompt):
    try:
        image = Image.open(image_file)
        response = model.generate_content([prompt, image], stream=False)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"


# Function: Record and transcribe voice prompt
def get_voice_prompt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Speak your prompt clearly...")
        audio = r.listen(source, timeout=5)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results; {e}"

st.set_page_config(page_title="Gemini Multimodal App", layout="wide")
st.title("🧠 Gemini Multimodal Prompting (Multiple Images + Voice)")

# Image uploader
image_files = st.file_uploader("Upload one or more images", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

# Text prompt or voice
prompt_option = st.radio("Choose input method for prompt:", ["📝 Text", "🎤 Voice"])

# Text box or voice recording
prompt = ""
if prompt_option == "📝 Text":
    prompt = st.text_area("Enter your prompt here")
elif prompt_option == "🎤 Voice":
    if st.button("🎙️ Record Prompt"):
        prompt = get_voice_prompt()
        st.success(f"🗣️ Transcribed Prompt: {prompt}")

# Process button
if st.button("🚀 Generate Multimodal Responses"):
    if image_files and prompt:
        for idx, img in enumerate(image_files):
            st.markdown(f"---\n### 🖼️ Image {idx+1}")
            st.image(img, width=300)
            with st.spinner(f"Processing Image {idx+1}..."):
                result = process_image_with_prompt(img, prompt)
                st.success("Response:")
                st.write(result)
    else:
        st.warning("Upload at least one image and provide a prompt.")
