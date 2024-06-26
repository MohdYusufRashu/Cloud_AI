# Use the official Python image as a base image
FROM python:3.9.17-bookworm

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PORT 8080
#ENV GOOGLE_APPLICATION_CREDENTIALS="gs://my-deployment-bucket325/service-account-key.json"
# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app

# Define the command to run your Flask app when the container starts
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
