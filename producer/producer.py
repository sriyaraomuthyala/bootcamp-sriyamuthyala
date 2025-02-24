import time
import requests

API_URL = "http://localhost:8000/enqueue/"

while True:
    job_data = "Job data example"
    response = requests.post(API_URL, json={"job_data": job_data})
    print(response.json())
    time.sleep(5)
