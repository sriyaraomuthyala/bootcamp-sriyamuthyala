import sqlite3
import os

DB_FILE = "queue.db"


class PersistentQSQLite:
    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.setup()

    def setup(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS queue (
            job_id TEXT PRIMARY KEY,
            job_data TEXT,
            status TEXT DEFAULT 'pending'
        )
        """)
        self.conn.commit()

    def enqueue(self, job_id, job_data):
        self.cursor.execute(
            "INSERT INTO queue (job_id, job_data, status, created_at) VALUES (?, ?, 'pending', CURRENT_TIMESTAMP)",
            (job_id, job_data),
        )
        self.conn.commit()

    def dequeue(self):
        self.cursor.execute(
            "SELECT job_id, job_data FROM queue WHERE status = 'pending' LIMIT 1")
        job = self.cursor.fetchone()
        if job:
            self.cursor.execute(
                "UPDATE queue SET status = 'processing' WHERE job_id = ?", (job[0],))
            self.conn.commit()
            return {"job_id": job[0], "job_data": job[1]}
        return None

    def mark_done(self, job_id):
        self.cursor.execute(
            "UPDATE queue SET status = 'done' WHERE job_id = ?", (job_id,))
        self.conn.commit()
