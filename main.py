from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image, ImageOps, ImageFilter
import pytesseract
import io
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

app = FastAPI(title="Image to Text API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

ALLOWED_TYPES = {"image/png", "image/jpeg", "image/webp", "image/bmp"}


def preprocess(img: Image.Image) -> Image.Image:
    img = img.convert("L")  # grayscale

    # Upscale small images (Tesseract performs best around 300 DPI)
    w, h = img.size
    if max(w, h) < 2200:
        scale = 2200 / max(w, h)
        img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)

    img = ImageOps.autocontrast(img)
    img = img.filter(ImageFilter.MedianFilter(size=3))  # denoise
    img = img.filter(ImageFilter.SHARPEN)
    return img


PSM_CANDIDATES = ["--oem 1 --psm 6", "--oem 1 --psm 3", "--oem 1 --psm 4"]


def best_ocr_result(img: Image.Image):
    best = None
    for config in PSM_CANDIDATES:
        data = pytesseract.image_to_data(img, config=config, output_type=pytesseract.Output.DICT)
        confidences = [int(c) for c, w in zip(data["conf"], data["text"]) if w.strip() and c != "-1"]
        avg_conf = sum(confidences) / len(confidences) if confidences else 0
        if best is None or avg_conf > best[0]:
            best = (avg_conf, data, config)
    return best  # (avg_conf, data, config)


@app.post("/api/extract-text")
async def extract_text(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(400, "Unsupported file type")

    start = time.time()
    raw = await file.read()

    try:
        img = Image.open(io.BytesIO(raw))
    except Exception:
        raise HTTPException(400, "Invalid image file")

    processed = preprocess(img)

    avg_conf, data, config = best_ocr_result(processed)
    words = [w for w in data["text"] if w.strip()]

    text = pytesseract.image_to_string(processed, config=config).strip()
    avg_conf = round(avg_conf, 2)

    return {
        "text": text,
        "confidence": avg_conf,
        "word_count": len(words),
        "processing_time_ms": round((time.time() - start) * 1000, 2),
    }


@app.get("/api/health")
async def health():
    return {"status": "ok"}
