from fastapi import FastAPI, UploadFile, File
import tempfile
from app.ingestion.file_processor import process_file

app = FastAPI()

@app.post("/upload-document/")
async def upload_document(file: UploadFile = File(...)):
    # Save temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=file.filename) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    content = process_file(tmp_path)
    return {"filename": file.filename, "content_preview": content[:500]}


@app.get("/")
def read_root():
    return {"message": "Generative AI Capstone Project is running!"}

# Health check endpoint
@app.get("/health-check")
def health_check():
    return {"status": "API is up and running"}


# Ask questions endpoint
@app.post("/ask-questions/")
async def ask_question(question: str):
    # Placeholder response
    return {"question": question, "answer": "LLM response will go here"}

