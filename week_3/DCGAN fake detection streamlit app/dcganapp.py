
import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

st.title("Dog/Cat Real-or-Fake Checker")
st.write("Upload a 64×64 image of a dog or cat to check if it's real or GAN-generated.")

disc = load_model("../generator.h5", compile=False)  # fix path

uploaded = st.file_uploader("Upload Image", type=["jpg","png"])
if uploaded:
    img = Image.open(uploaded).resize((64,64))
    st.image(img, caption="Uploaded Image", use_column_width=True)
    img_arr = np.array(img)/127.5 - 1
    img_arr = np.expand_dims(img_arr, axis=0)

    if st.button("Check"):
        score = disc.predict(img_arr)[0][0]
        label = "REAL" if score > 0.5 else "FAKE"
        st.write(f"Discriminator confidence: **{score:.2f}** → {label}")
