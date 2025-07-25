
# model/tokenizer.py
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

class CustomTokenizer:
    def __init__(self, num_words=2000):
        self.tokenizer = Tokenizer(num_words=num_words, oov_token='<OOV>')
    
    def fit(self, texts):
        self.tokenizer.fit_on_texts(texts)
    
    def texts_to_seqs(self, texts):
        return self.tokenizer.texts_to_sequences(texts)
    
    def pad_sequences(self, seqs, maxlen=None):
        return pad_sequences(seqs, maxlen=maxlen, padding='post')

    def save(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self.tokenizer, f)

    def load(self, path):
        with open(path, 'rb') as f:
            self.tokenizer = pickle.load(f)
