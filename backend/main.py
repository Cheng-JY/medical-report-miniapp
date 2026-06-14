from fastapi import FastAPI, UploadFile, File
from pathlib import Path

app = FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@app.get("/")
def root():
    return {"message": "Medical Report API is running"}


@app.post("/upload-report")
async def upload_report(file: UploadFile = File(...)):
    save_path = UPLOAD_DIR / file.filename

    content = await file.read()
    with open(save_path, "wb") as f:
        f.write(content)

    return {
        "message": "uploaded successfully",
        "filename": file.filename
    }