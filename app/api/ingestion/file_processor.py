import os
import csv
import pandas as pd
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import pytesseract

def process_file(file_path: str) -> str:
    """
    Process a file and return its text content.
    Supports TXT, CSV, XLSX, and PDF (with OCR fallback).
    """
    ext = os.path.splitext(file_path)[1].lower()
    text = ""

    try:
        if ext == ".txt":
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()

        elif ext == ".csv":
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                reader = csv.reader(f)
                text = "\n".join([", ".join(row) for row in reader])

        elif ext == ".xlsx":
            df = pd.read_excel(file_path)
            text = df.to_string()

        elif ext == ".pdf":
            # Try extracting text with PyPDF2
            reader = PdfReader(file_path)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

            # Fallback to OCR if no text found
            if not text.strip():
                images = convert_from_path(file_path)
                text = " ".join(pytesseract.image_to_string(img) for img in images)

        else:
            text = "Unsupported file format"

    except Exception as e:
        text = f"Error processing file: {str(e)}"

    return text
