# Image to Text (OCR Web App)

A simple web app that extracts text from images using Optical Character Recognition (OCR). Upload an image, click extract, and get clean, copyable text — with confidence score, word count, and processing time.

**Live:** https://image-to-text-production-16e2.up.railway.app

## Features

- Drag & drop or click to upload images (PNG, JPG, WEBP, BMP)
- Live image preview before extraction
- Text extraction powered by Tesseract OCR
- Image preprocessing (grayscale, upscaling, denoising, sharpening) for better accuracy
- Shows confidence %, word count, and processing time
- One-click copy to clipboard
- Clean, dark-themed responsive UI

## Tech Stack

**Backend:** Python, FastAPI, Tesseract OCR (pytesseract), Pillow
**Frontend:** HTML, CSS, JavaScript (vanilla, no frameworks)
**Deployment:** Docker, Railway

## Project Structure

```
IMAGE-TO-TEXT/
├── main.py             # FastAPI server + OCR logic (also serves frontend)
├── requirements.txt    # Python dependencies
├── index.html           # Web UI
├── Dockerfile           # Container build for deployment
└── start.bat             # One-click start (Windows, local dev)
```

## Setup & Installation

### Prerequisites

- Python 3.8+
- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) installed on your system

### Run it locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Open your browser and go to **`http://localhost:8000`** — the backend also serves the frontend, so no separate step is needed.

Windows users can also just double-click `start.bat` to launch the server and open the site automatically.

### Access from your phone (same WiFi)

1. Run the server with: `uvicorn main:app --reload --host 0.0.0.0 --port 8000`
2. Find your laptop's local IP with `ipconfig` (look for "IPv4 Address")
3. On your phone's browser, go to `http://<your-ip>:8000`

### Run with Docker

```bash
docker build -t image-to-text .
docker run -p 8000:8000 -e PORT=8000 image-to-text
```

## API Endpoints

| Method | Endpoint             | Description                          |
|--------|-----------------------|---------------------------------------|
| POST   | `/api/extract-text`   | Upload an image, get extracted text   |
| GET    | `/api/health`         | Health check                          |

Interactive API docs available at `/docs`.

### Example Response

```json
{
  "text": "Extracted text from the image...",
  "confidence": 94.32,
  "word_count": 128,
  "processing_time_ms": 842.15
}
```

## Notes

- OCR accuracy typically ranges from 90–96% depending on image quality, font, and resolution.
- For best results, use clear, high-resolution, well-lit images with minimal skew.

### Tosif Rayan [GitHub](https://github.com/mrtosif222)

![GitHub](https://img.shields.io/badge/GitHub-mrtosif222-181717?style=flat&logo=github)
