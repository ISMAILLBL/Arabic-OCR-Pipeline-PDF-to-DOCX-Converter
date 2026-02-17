# 📄 Arabic OCR Pipeline – PDF to DOCX Converter

A full OCR pipeline built with **Flask + Celery + Redis + Tesseract** that converts scanned Arabic PDF files into editable Word (.docx) documents.

This project supports asynchronous processing using Celery workers and provides a simple web interface for uploading PDFs and downloading the generated DOCX files.

---

## 🚀 Features

- 📤 Upload scanned PDF files
- 🔎 Arabic OCR using Tesseract
- 🔄 Asynchronous processing with Celery
- ⚡ Redis as message broker & result backend
- 📄 Automatic DOCX generation
- 🌐 Simple Flask web interface
- 🖥 Windows-compatible (Celery `--pool=solo`)

---

## 🏗 Architecture

User Upload  
⬇  
Flask Web App  
⬇  
Celery Task Queue  
⬇  
Redis Broker  
⬇  
OCR Processing (Tesseract + pdf2image)  
⬇  
DOCX Generation  

---

## 🛠 Tech Stack

- Python 3.10+
- Flask
- Celery
- Redis
- Tesseract OCR
- pdf2image
- python-docx
- Pillow

---

## 📂 Project Structure
