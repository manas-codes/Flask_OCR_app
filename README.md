# Flask_OCR_app

This is a simple Flask application that provides OCR (Optical Character Recognition) capabilities using Tesseract. The application exposes an API to extract text and bounding boxes from images.

## Features

- Extract text from images.
- Get bounding boxes for words, lines, paragraphs, blocks, and pages.

## Requirements

- Docker
- An internet connection to pull the Docker image

## Quick Start

### To Pull Docker Image

To pull the Docker image from Docker Hub, run:

```
docker pull manascodes4/ocr-api
```

### Run the Docker Container

To run the Docker container, use the following command:

```
docker run -p 8000:8000 manascodes4/ocr-api
```

This command will start the Flask application on port 8000.

### Access the API

Once the container is running, the API can be accessed at `http://localhost:8000`.

## Running Locally

If you want to run the Flask app locally, follow these steps:

1. clone the repository, run:

```bash
git clone https://github.com/manas-codes/Flask_OCR_app.git
cd Flask_OCR_app
```
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Make sure Tesseract OCR is installed on your system. You can download it from [here](https://github.com/tesseract-ocr/tesseract).

4. Run the Flask app:

```bash
python api.py
```

The Flask application will start, and you can access the API at `http://localhost:8000`.

## API Documentation

For detailed API documentation, visit the [Postman Documentation](https://documenter.getpostman.com/view/29726683/2sA3QzZo4c).

### Endpoints

#### Get Text from Image

- **URL:** `/api/get-text`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "base64_image": "base64_encoded_image_string"
  }
  ```

#### Get Bounding Boxes from Image

- **URL:** `/api/get-bboxes`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "base64_image": "base64_encoded_image_string",
    "bbox_type": "word" // can be word, line, paragraph, block, or page
  }
  ```

