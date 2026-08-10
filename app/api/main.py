import os
import tempfile
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from .ingestion.file_processor import process_file
from .ingestion.embedding import embed_chunks, search_chunks

app = FastAPI()

# Allow Streamlit frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global store for uploaded chunks
uploaded_chunks = []

@app.get("/health-check")
async def health_check():
    return {"status": "ok"}

@app.post("/upload-document/")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a document, extract text, chunk it, embed chunks into FAISS.
    """
    ext = os.path.splitext(file.filename)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    # Extract + chunk
    chunks = process_file(tmp_path)

    # Store globally for demo
    global uploaded_chunks
    uploaded_chunks = chunks

    # Embed and save FAISS index
    embed_chunks(chunks)

    return {
        "filename": file.filename,
        "chunks_preview": chunks[:5]  # show first few chunks
    }

@app.post("/ask-questions/")
async def ask_questions(question: str = Form(...)):
    """
    Ask a question: embed query, search FAISS, return top chunks.
    """
    global uploaded_chunks
    if not uploaded_chunks:
        return {"answer": "No document uploaded yet."}

    results = search_chunks(question, uploaded_chunks)

    return {
        "question": question,
        "top_chunks": results
    }
