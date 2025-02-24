from fastapi import FastAPI
from persistent_queue.persistent_queue import PersistentQSQLite
import uuid

app = FastAPI()
queue = PersistentQSQLite()

@app.get("/")  
def read_root():
    return {"message": "Hello, FastAPI is working!"}

@app.post("/enqueue/")
def enqueue_job(job_data: str):
    job_id = str(uuid.uuid4())
    queue.enqueue(job_id, job_data)
    return {"message": "Job enqueued", "job_id": job_id}

@app.get("/dequeue/")
def dequeue_job():
    job = queue.dequeue()
    if job:
        job_id, job_data = job
        return {"job_id": job_id, "job_data": job_data}
    return {"message": "No pending jobs"}

@app.post("/mark_done/{job_id}")
def mark_done(job_id: str):
    queue.mark_done(job_id)
    return {"message": f"Job {job_id} marked as done"}
