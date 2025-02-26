import time
from persistent_queue.queue_manager import QueueManager

class QueueConsumer:
    def __init__(self):
        """Initialize the consumer with the QueueManager."""
        self.queue = QueueManager()

    def process_job(self, job_id, job_data):
        """Simulate job processing."""
        try:
            print(f"🚀 Processing job {job_id}: {job_data}")
            time.sleep(2)  # Simulate processing delay
            self.queue.mark_done(job_id)
            print(f"✅ Job {job_id} completed.")
        except Exception as e:
            print(f"❌ Error processing job {job_id}: {e}")
            self.queue.mark_failed(job_id)

    def consume(self):
        """Continuously fetch and process jobs."""
        while True:
            job = self.queue.fetch_next_job()  # ✅ Fixed call to correct method
            if job:
                job_id, job_data = job
                print(f"🔄 Retrying job {job_id}")

                self.process_job(job_id, job_data)
            else:
                print("✅ No pending jobs. Sleeping...")
                time.sleep(5)  # Sleep before checking again

if __name__ == "__main__":
    consumer = QueueConsumer()
    consumer.consume()
