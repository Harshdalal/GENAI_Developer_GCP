# Use Python
FROM python:3.11-slim

# Set folder
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY main.py .
COPY agents.py .

# Install packages
RUN pip install -r requirements.txt

# Set port
ENV PORT=8501

# Start the app
CMD streamlit run main.py --server.port=$PORT --server.address=0.0.0.0