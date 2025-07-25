

import tensorflow as tf
from tensorflow.keras.layers import Embedding, Dense, LayerNormalization, Dropout
import numpy as np

class PositionalEncoding(tf.keras.layers.Layer):
    def __init__(self, position, d_model):
        super().__init__()
        angle_rads = self.get_angles(np.arange(position)[:, np.newaxis],
                                     np.arange(d_model)[np.newaxis, :],
                                     d_model)
        angle_rads[:, 0::2] = np.sin(angle_rads[:, 0::2])
        angle_rads[:, 1::2] = np.cos(angle_rads[:, 1::2])
        self.pos_encoding = tf.cast(angle_rads[np.newaxis, ...], dtype=tf.float32)

    def get_angles(self, pos, i, d_model):
        angle_rates = 1 / np.power(10000, (2 * (i//2)) / np.float32(d_model))
        return pos * angle_rates

    def call(self, x):
        return x + self.pos_encoding[:, :tf.shape(x)[1], :]

def transformer_encoder(num_layers, d_model, num_heads, dff, input_vocab_size, maximum_position_encoding):
    inputs = tf.keras.Input(shape=(None,))
    padding_mask = tf.keras.Input(shape=(1, 1, None))

    x = Embedding(input_vocab_size, d_model)(inputs)
    x = PositionalEncoding(maximum_position_encoding, d_model)(x)

    for _ in range(num_layers):
        attn_output = tf.keras.layers.MultiHeadAttention(num_heads=num_heads, key_dim=d_model)(x, x, attention_mask=padding_mask)
        x = LayerNormalization(epsilon=1e-6)(x + attn_output)
        ffn_output = Dense(dff, activation='relu')(x)
        ffn_output = Dense(d_model)(ffn_output)
        x = LayerNormalization(epsilon=1e-6)(x + ffn_output)

    return tf.keras.Model(inputs=[inputs, padding_mask], outputs=x)
