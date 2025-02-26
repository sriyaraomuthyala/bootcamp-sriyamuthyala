import sqlite3
import uuid
import threading

# SQLite Database File
DB_FILE = "/home/sriyaraomuthyala/bootcamp-sriyamuthyala/Persistent_Queue_System/queue.db"

class QueueManager:
    def __init__(self):
        """Initialize the queue manager with an SQLite connection."""
        self.lock = threading.Lock()  # Prevents race conditions
        self.conn = sqlite3.connect(DB_FILE, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._setup_db()

    def _setup_db(self):
        """Ensure the queue table exists with the correct schema."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS queue (
                job_id TEXT PRIMARY KEY,
                job_data TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                attempts INTEGER NOT NULL DEFAULT 0
            )
        """)
        self.conn.commit()

    def enqueue(self, job_data):
        """Add a new job to the queue."""
        with self.lock:
            job_id = str(uuid.uuid4())
            self.cursor.execute(
                "INSERT INTO queue (job_id, job_data, status, attempts) VALUES (?, ?, 'pending', 0)",
                (job_id, job_data)
            )
            self.conn.commit()
        return job_id

    def fetch_next_job(self):
        """Fetch a pending job with less than 3 attempts and mark it as processing."""
        with self.lock:
            self.cursor.execute("""
                SELECT job_id, job_data FROM queue 
                WHERE status = 'pending' AND attempts < 3
                ORDER BY created_at ASC 
                LIMIT 1
            """)
            job = self.cursor.fetchone()

            if job:
                job_id = job[0]
                self.cursor.execute("UPDATE queue SET status = 'processing', attempts = attempts + 1 WHERE job_id = ?", (job_id,))
                self.conn.commit()
                return job
        return None

    def mark_done(self, job_id):
        """Mark a job as completed."""
        with self.lock:
            self.cursor.execute("UPDATE queue SET status = 'completed' WHERE job_id = ?", (job_id,))
            self.conn.commit()

    def mark_failed(self, job_id):
        """Mark a job as failed if it has exceeded 3 attempts."""
        with self.lock:
            self.cursor.execute("UPDATE queue SET status = 'failed' WHERE job_id = ?", (job_id,))
            self.conn.commit()

    def retry_failed_jobs(self):
        """Reset jobs stuck in processing back to pending if they have not exceeded 3 attempts."""
        with self.lock:
            self.cursor.execute("""
                UPDATE queue 
                SET status = 'pending' 
                WHERE status = 'processing' AND attempts < 3
            """)
            self.conn.commit()
