import sqlite3

conn = sqlite3.connect("queue.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS queue (
    job_id TEXT PRIMARY KEY,
    job_data TEXT,
    status TEXT DEFAULT 'pending'
)
""")
conn.commit()
conn.close()
