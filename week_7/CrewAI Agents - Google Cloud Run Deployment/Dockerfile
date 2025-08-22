# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (leverages Docker cache for faster builds)
COPY requirements.txt .

# Install dependencies (use --no-cache-dir to reduce image size)
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY main.py .
COPY agents.py .

# Expose the port Streamlit will run on
ENV PORT=8501

# Recommended CMD format (exec form to handle signals correctly)
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
