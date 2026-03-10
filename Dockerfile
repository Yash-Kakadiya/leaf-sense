# Use the official Python 3.10 image to match your training environment
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Hugging Face Spaces run as a non-root user. 
# We need to give write permissions to the /app folder so Flask can save uploaded images.
RUN chmod -R 777 /app

# Hugging Face Spaces require the app to run on port 7860
EXPOSE 7860

# Command to run the Flask app using Gunicorn on port 7860
CMD ["gunicorn", "-b", "0.0.0.0:7860", "--workers", "1", "--threads", "2", "--timeout", "120", "app:app"]