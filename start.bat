@echo off
title Image to Text - OCR Website
echo Starting backend server...
start cmd /k "uvicorn main:app --reload --port 8000"
timeout /t 3 /nobreak >nul
echo Opening website...
start index.html
