
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install Tesseract-OCR
RUN apt-get update && apt-get install -y tesseract-ocr && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file from the app directory into the container
COPY app/requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run the application
CMD ["python", "app/api.py"]

