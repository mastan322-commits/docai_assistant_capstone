import os
import pandas as pd
import json
import yaml
from PyPDF2 import PdfReader

def process_file(file_path: str):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    elif ext == ".pdf":
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    elif ext == ".csv":
        df = pd.read_csv(file_path)
        return df.to_string()

    elif ext in [".xls", ".xlsx"]:
        df = pd.read_excel(file_path)
        return df.to_string()

    elif ext == ".json":
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return json.dumps(data, indent=2)

    elif ext in [".yaml", ".yml"]:
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return yaml.dump(data)

    else:
        return "Unsupported file format"
