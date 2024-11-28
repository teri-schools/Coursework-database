FROM python:3.12-slim

# Environment settings
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create app directory
RUN mkdir /app
WORKDIR /app

# Add system-level dependencies (including gcc and npm)
# RUN apt-get update
# Install Python dependencies from requirements.txt and cache the layer
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application code
ADD . /app

RUN pip install -r requirements.txt

# Expose port 8000 for FastAPI
EXPOSE 8000