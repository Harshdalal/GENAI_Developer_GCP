# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy code to container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

