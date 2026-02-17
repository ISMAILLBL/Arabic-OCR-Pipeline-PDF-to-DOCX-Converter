# 📄 OCR Pipeline -- PDF to DOCX (Arabic Supported)

Web application that converts scanned PDF files into Word (.docx)
documents using OCR.

Built with Flask, Celery, Redis and Tesseract OCR.

------------------------------------------------------------------------

## Features

-   Upload PDF
-   OCR text extraction
-   Arabic language support
-   Generate DOCX automatically
-   Asynchronous processing (Celery)
-   Queue management (Redis)

------------------------------------------------------------------------

## Architecture

Flask → Celery → Redis → Tesseract → python-docx

------------------------------------------------------------------------

## Tech Stack

Python, Flask, Celery, Redis, Tesseract OCR, pdf2image, pytesseract,
python-docx, Pillow

------------------------------------------------------------------------

## Run

1.  Install dependencies pip install -r requirements.txt

2.  Start Redis redis-server

3.  Start worker celery -A tasks.celery worker --loglevel=info
    --pool=solo

4.  Start app python app.py

------------------------------------------------------------------------

Author: Ismail
