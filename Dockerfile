# Use a lightweight Python 3.12 image
FROM python:3.12-slim

# Install ffmpeg (Required by Whisper for audio processing)
RUN apt-get update && apt-get install -y ffmpeg

# Set the working directory inside the container
WORKDIR /app

# Copy just the requirements first to leverage Docker caching
COPY requirements.txt .

# Install dependencies. The --no-cache-dir keeps the container small!
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app files (main.py, static folder, etc.)
COPY . .

# Start the FastAPI server, binding to Railway's dynamic PORT
CMD uvicorn main:app --host 0.0.0.0 --port $PORT