
# Use official lightweight Python image with a specific version for consistency
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy only requirements first for caching
COPY requirements.txt .

# Upgrade pip and install dependencies without cache to reduce image size
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port your Flask app listens on
EXPOSE 5000

# Use environment variables for Flask configuration (optional but good practice)

# Run the Flask app using the built-in server (suitable for dev)
# For production, you might replace this with Gunicorn or uWSGI
CMD ["python", "app.py"]
