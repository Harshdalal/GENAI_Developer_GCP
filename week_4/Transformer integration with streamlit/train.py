# model/train.py
from utils.data_loader import load_data
from model.tokenizer import CustomTokenizer
import tensorflow as tf
import os

def train_model():
    en_texts, hi_texts = load_data()

    en_tokenizer = CustomTokenizer()
    hi_tokenizer = CustomTokenizer()
    en_tokenizer.fit(en_texts)
    hi_tokenizer.fit(hi_texts)

    # Tokenize and pad
    en_seqs = en_tokenizer.texts_to_seqs(en_texts)
    hi_seqs = hi_tokenizer.texts_to_seqs(hi_texts)
    
    max_len = 5
    en_seqs = en_tokenizer.pad_sequences(en_seqs, maxlen=max_len)
    hi_seqs = hi_tokenizer.pad_sequences(hi_seqs, maxlen=max_len)

    vocab_size = 2000

    # Build a simple Seq2Seq model
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=64, input_length=max_len),
        tf.keras.layers.LSTM(128, return_sequences=True),
        tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(vocab_size, activation='softmax'))
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Reshape target: (samples, sequence_len, 1)
    hi_seqs = hi_seqs.reshape((hi_seqs.shape[0], hi_seqs.shape[1], 1))

    model.fit(en_seqs, hi_seqs, epochs=300, verbose=1)

    if not os.path.exists("checkpoints"):
        os.mkdir("checkpoints")
    model.save("checkpoints/model.h5")
    en_tokenizer.save("checkpoints/en_tokenizer.pkl")
    hi_tokenizer.save("checkpoints/hi_tokenizer.pkl")
