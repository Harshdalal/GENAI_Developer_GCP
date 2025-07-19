
# app.py
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import io

# Load the trained model
model = load_model('trained_model.h5')

# Streamlit UI
st.set_page_config(page_title="Pneumonia Detector", layout="centered")
st.title("🩻 Pneumonia Detection from Chest X-Ray")
st.write("Upload a chest X-ray image to check for **Pneumonia** vs **Normal**.")

# File uploader
uploaded_file = st.file_uploader("Choose a chest X-ray image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image_data = Image.open(uploaded_file)
    st.image(image_data, caption='Uploaded Image', use_column_width=True)

    if st.button("Predict"):
        # Preprocess the image
        img = image_data.resize((150, 150))
        img_tensor = image.img_to_array(img) / 255.0
        img_tensor = np.expand_dims(img_tensor, axis=0)

        prediction = model.predict(img_tensor)[0][0]
        result = "🟡 Pneumonia Detected" if prediction > 0.5 else "🟢 Normal"

        st.subheader("🔍 Prediction Result")
        st.success(f"**{result}** (Confidence: {prediction:.2f})")
