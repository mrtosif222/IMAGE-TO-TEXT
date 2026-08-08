# Image to Text (OCR Web App)

A simple web app that extracts text from images using Optical Character Recognition (OCR). Upload an image, click extract, and get clean, copyable text — with confidence score, word count, and processing time.

## Features

- Drag & drop or click to upload images (PNG, JPG, WEBP, BMP)
- Live image preview before extraction
- Text extraction powered by Tesseract OCR
- Image preprocessing (grayscale, upscaling, denoising, sharpening) for better accuracy
- Auto-selects the best OCR mode (PSM) per image for higher accuracy
- Shows confidence %, word count, and processing time
- One-click copy to clipboard
- Clean, dark-themed responsive UI

## Tech Stack

**Backend:** Python, FastAPI, Tesseract OCR (pytesseract), Pillow
**Frontend:** HTML, CSS, JavaScript (vanilla, no frameworks)

## Project Structure

```
IMAGE-TO-TEXT/
├── backend/
│   ├── main.py             # FastAPI server + OCR logic
│   └── requirements.txt    # Python dependencies
└── frontend/
    └── index.html          # Web UI
```

## Setup & Installation

### Prerequisites

- Python 3.8+
- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) installed on your system

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

> **Windows users:** If Tesseract isn't in your system PATH, set the path manually in `main.py`:
> ```python
> pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
> ```

The backend will run at `http://localhost:8000`.

### Frontend Setup

Just open `frontend/index.html` in your browser — no build step required.

## API Endpoints

| Method | Endpoint             | Description                          |
|--------|-----------------------|---------------------------------------|
| POST   | `/api/extract-text`   | Upload an image, get extracted text   |
| GET    | `/api/health`         | Health check                          |

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

## Author

**Tosif Rayan**
[GitHub](https://github.com/mrtosif222)
