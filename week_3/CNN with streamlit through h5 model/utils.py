
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image

def preprocess_image(img_pil, target_size=(150, 150)):
    """
    Preprocesses the uploaded PIL image for CNN model prediction.
    - Resizes the image
    - Converts to array
    - Scales pixel values to [0, 1]
    - Adds batch dimension
    """
    img = img_pil.resize(target_size)
    img_array = image.img_to_array(img) / 255.0
    return np.expand_dims(img_array, axis=0)
