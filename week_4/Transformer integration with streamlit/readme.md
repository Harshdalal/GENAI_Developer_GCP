# Project Structure

english_to_hindi_transformer/

├── app.py                      # ✅ Streamlit frontend

├── model/

│   ├── __init__.py

│   ├── transformer.py          # ✅ Transformer model (from scratch using Keras)

│   ├── train.py                # ✅ Training loop with synthetic/simple data

│   ├── tokenizer.py            # ✅ Tokenizer utilities

├── utils/

│   ├── data_loader.py          # ✅ Load or create sample dataset

│   └── translate.py            # ✅ Translation logic for inference

├── checkpoints/                # ⬆️ Saved model weights (after training)

├── requirements.txt

└── README.md

#✅ Step-by-Step Instructions

Step 1: 🔽 Clone or Setup Folder

CMD > mkdir english_to_hindi_transformer

CMD > cd english_to_hindi_transformer

Step 2: 📦 Create requirements.txt

pip install -r requirements.txt

📁 File: model/transformer.py

📁 File: model/tokenizer.py

📁 File: utils/data_loader.py

📁 File: model/train.py

📁 File: utils/translate.py

📁 File: app.py (Streamlit Frontend)

# Pre-Train to Avoid Runtime Delay

CMD > python -c "from model.train import train_model; train_model()"

after this h5 model will generate

# Then launch Streamlit:

CMD > streamlit run app.py






