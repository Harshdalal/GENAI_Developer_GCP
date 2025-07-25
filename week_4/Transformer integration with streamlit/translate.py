# utils/translate.py
import tensorflow as tf
from model.tokenizer import CustomTokenizer
import numpy as np

def translate(input_text):
    model = tf.keras.models.load_model("checkpoints/model.h5")
    en_tokenizer = CustomTokenizer(); en_tokenizer.load("checkpoints/en_tokenizer.pkl")
    hi_tokenizer = CustomTokenizer(); hi_tokenizer.load("checkpoints/hi_tokenizer.pkl")

    seq = en_tokenizer.texts_to_seqs([input_text])
    seq = en_tokenizer.pad_sequences(seq, maxlen=5)
    pred = model.predict(seq)

    pred_tokens = np.argmax(pred[0], axis=-1)
    inv_vocab = {v: k for k, v in hi_tokenizer.tokenizer.word_index.items()}

    return ' '.join([inv_vocab.get(tok, '') for tok in pred_tokens if tok != 0])
