import sqlite3
import argparse

DB_FILE = "queue.db"

class AdminManager:
    def __init__(self):
        #Initialize connection to SQLite database.
        self.conn = sqlite3.connect(DB_FILE)
        self.cursor = self.conn.cursor()

    def resubmit_failed_jobs(self):
        #Resets jobs stuck in 'processing' back to 'pending'
        self.cursor.execute("UPDATE queue SET status = 'pending' WHERE status = 'processing'")
        self.conn.commit()
        print("[INFO] Resubmitted failed jobs.")

    def mark_as_failed(self, job_id):
        #Marks a specific job as 'failed'
        self.cursor.execute("UPDATE queue SET status = 'failed' WHERE job_id = ?", (job_id,))
        self.conn.commit()
        print(f"[INFO] Marked job {job_id} as failed.")

    def reset_stuck_jobs(self):
        #Moves jobs that were 'processing' back to 'pending'.
        self.cursor.execute("UPDATE queue SET status = 'pending' WHERE status = 'processing'")
        self.conn.commit()
        print("[INFO] Reset stuck jobs to 'pending'.")

    def list_jobs(self, status=None):
        #Lists all jobs or filters by status
        if status:
            self.cursor.execute("SELECT * FROM queue WHERE status = ?", (status,))
        else:
            self.cursor.execute("SELECT * FROM queue")

        jobs = self.cursor.fetchall()
        if jobs:
            print(f"\n{'Job ID':<40} {'Status':<15} {'Data':<20}")
            print("=" * 80)
            for job in jobs:
                print(f"{job[0]:<40} {job[2]:<15} {job[1]:<20}")
        else:
            print("[INFO] No jobs found.")

     def close(self):
        #Closes the database connection.
        self.conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Admin tools for managing job queue.")
    parser.add_argument("--list", help="List all jobs (optionally filter by status)", nargs="?", const="all")
    parser.add_argument("--resubmit", action="store_true", help="Resubmit failed and stuck jobs")
    parser.add_argument("--reset-stuck", action="store_true", help="Reset stuck jobs (processing -> pending)")
    parser.add_argument("--fail", type=str, help="Mark a specific job as failed")

    args = parser.parse_args()
    admin = AdminManager()

    if args.list:
        status = None if args.list == "all" else args.list
        admin.list_jobs(status)

    if args.resubmit:
        admin.resubmit_jobs()

    if args.reset_stuck:
        admin.reset_stuck_jobs()

    if args.fail:
        admin.mark_as_failed(args.fail)

    admin.close()
