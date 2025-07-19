
import tensorflow as tf
from tensorflow.keras.layers import Conv2D, Conv2DTranspose, Dense, Flatten, Reshape, LeakyReLU, BatchNormalization
from tensorflow.keras import Sequential
from tensorflow.keras.optimizers import Adam
import numpy as np
import os
from glob import glob
from PIL import Image

# Hyperparameters
img_size = 64
latent_dim = 100
batch_size = 64
epochs = 5000

# Load images
def load_images(folder):
    paths = glob(os.path.join(folder, '*/*.jpg'))
    imgs = [np.array(Image.open(p).resize((img_size, img_size))) for p in paths]
    return np.array(imgs)

images = load_images(os.path.join(path, 'train'))
images = (images - 127.5) / 127.5  # Scale to [-1,1]
dataset = tf.data.Dataset.from_tensor_slices(images).shuffle(1000).batch(batch_size)

# Build Generator
def build_generator():
    model = Sequential([
        Dense(8*8*256, input_dim=latent_dim),
        Reshape((8,8,256)),
        BatchNormalization(), LeakyReLU(),
        Conv2DTranspose(128, (4,4), strides=(2,2), padding='same'),
        BatchNormalization(), LeakyReLU(),
        Conv2DTranspose(64, (4,4), strides=(2,2), padding='same'),
        BatchNormalization(), LeakyReLU(),
        Conv2DTranspose(3, (4,4), strides=(2,2), padding='same', activation='tanh')
    ])
    return model

# Build Discriminator
def build_discriminator():
    model = Sequential([
        tf.keras.Input(shape=(img_size,img_size,3)),
        Conv2D(64, (4,4), strides=(2,2), padding='same'),
        LeakyReLU(),
        Conv2D(128, (4,4), strides=(2,2), padding='same'),
        BatchNormalization(), LeakyReLU(),
        Flatten(),
        Dense(1, activation='sigmoid')
    ])
    return model

# Instantiate
generator = build_generator()
discriminator = build_discriminator()
discriminator.compile(optimizer=Adam(0.0002), loss='binary_crossentropy')

# GAN assembly
discriminator.trainable = False
gan = Sequential([generator, discriminator])
gan.compile(optimizer=Adam(0.0002), loss='binary_crossentropy')

# Training loop
for epoch in range(epochs):
    for real in dataset:
        noise = np.random.normal(0,1,(batch_size,latent_dim))
        fake = generator.predict(noise)
        d_loss = 0.5*(discriminator.train_on_batch(real, np.ones((len(real),1))) +
                      discriminator.train_on_batch(fake, np.zeros((batch_size,1))))
        g_loss = gan.train_on_batch(noise, np.ones((batch_size,1)))

    if epoch % 500 == 0:
        print(f"[Epoch {epoch}] D loss: {d_loss:.4f}, G loss: {g_loss:.4f}")

# Save models
generator.save('generator.h5')
discriminator.save('discriminator.h5')
print("✅ Models saved")
