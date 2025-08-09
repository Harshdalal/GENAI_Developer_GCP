# Dockerfile

# 1. Base image
FROM python:3.10-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set working directory
WORKDIR /app

# 4. Copy all files
COPY . .

# 5. Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 6. Expose Streamlit port
EXPOSE 8080

# 7. Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
