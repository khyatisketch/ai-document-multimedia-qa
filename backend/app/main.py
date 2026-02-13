from fastapi import FastAPI

app = FastAPI(title="AI Document & Multimedia Q&A")

@app.get("/")
def health():
    return {"status": "running"}