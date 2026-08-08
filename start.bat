@echo off
title Image to Text - OCR Website
echo Starting backend server...
start cmd /k "uvicorn main:app --reload --host 0.0.0.0 --port 8000"
timeout /t 3 /nobreak >nul
echo Opening website...
start http://localhost:8000
