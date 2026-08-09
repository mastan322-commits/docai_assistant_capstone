from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Generative AI Capstone Project is running!"}
