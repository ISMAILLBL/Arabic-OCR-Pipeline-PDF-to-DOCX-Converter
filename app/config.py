import os
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", os.path.join(BASE_DIR, "uploads"))
RESULT_FOLDER = os.getenv("RESULT_FOLDER", os.path.join(BASE_DIR, "results"))
TESSERACT_CMD = os.getenv("TESSERACT_CMD", "tesseract")  # si tesseract est sur PATH
OCR_LANG = os.getenv("OCR_LANG", "ara")  # 'ara' pour arabe
