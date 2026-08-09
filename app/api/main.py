from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Generative AI Capstone Project is running!"}

# Health check endpoint
@app.get("/health-check")
def health_check():
    return {"status": "API is up and running"}

# Upload document endpoint
@app.post("/upload-document/")
async def upload_document(file: UploadFile = File(...)):
    content = await file.read()
    # Later: parse PDF/TXT/CSV and store in vector DB
    return {"filename": file.filename, "size": len(content)}

# Ask questions endpoint
@app.post("/ask-questions/")
async def ask_question(question: str):
    # Placeholder response
    return {"question": question, "answer": "LLM response will go here"}

