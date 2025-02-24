import time
import requests

DEQUEUE_URL = "http://localhost:8000/dequeue/"
MARK_DONE_URL = "http://localhost:8000/mark_done/"

while True:
    response = requests.get(DEQUEUE_URL)
    job = response.json()
    
    if "job_id" in job:
        job_id = job["job_id"]
        print(f"Processing job: {job_id}")
        time.sleep(10)  # Simulate processing time
        requests.post(f"{MARK_DONE_URL}{job_id}")
        print(f"Completed job: {job_id}")
