# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt (create this file with dependencies)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy API code into container
COPY . .

# Expose Flask port
EXPOSE 5000

# Run the Flask API
CMD ["python", "flask_api.py"]
