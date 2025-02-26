import time
from persistent_queue.queue_manager import QueueManager

queue = QueueManager()

if __name__ == "__main__":
    while True:
        job_id = queue.submit_job(f"Process file {int(time.time())}")  
        print(f"✅ Job {job_id} added to queue.")
        time.sleep(5)  # Simulating periodic job submissions
