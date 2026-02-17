import os
import uuid
from celery import Celery
from config import REDIS_URL, UPLOAD_FOLDER, RESULT_FOLDER, OCR_LANG
from ocr_utils import pdf_to_images, image_to_text, normalize_arabic_text, assemble_docx

celery = Celery('tasks', broker=REDIS_URL, backend=REDIS_URL)

@celery.task(bind=True)
def process_pdf(self, filename):
    """Tâche Celery: prend un PDF en entrée, renvoie path docx"""
    pdf_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(pdf_path)

    images = pdf_to_images(pdf_path)
    text_blocks = []
    for i, img in enumerate(images):
        raw = image_to_text(img)
        clean = normalize_arabic_text(raw)
        text_blocks.append(clean)

    # assemble into docx
    basename = os.path.splitext(filename)[0]
    out_name = f"{basename}.docx"
    out_path = os.path.join(RESULT_FOLDER, out_name)
    assemble_docx(text_blocks, out_path)
    return {"docx": out_name}
