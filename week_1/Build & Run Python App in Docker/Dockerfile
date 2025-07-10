# Use official Python base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy local files to container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port to outside Docker
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
