from fastapi import FastAPI, UploadFile, File, status
import tempfile
from app.api.ingestion.file_processor import process_file
from pydantic import BaseModel

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
@app.get("/health-check", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "API is up and running"}

# Define the Question model first
class Question(BaseModel):
    question: str

# Ask questions endpoint
@app.post("/ask-questions/")
def ask_questions(data: Question):
    return {"answer": f"You asked: {data.question}"}
