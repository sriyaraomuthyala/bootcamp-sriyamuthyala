from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/upload/")
def upload_file(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        buffer.write(file.file.read())
    return {"filename": file.filename}