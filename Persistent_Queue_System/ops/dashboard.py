import streamlit as st
import sqlite3
import pandas as pd
import requests

#  API Base URL (Update when running externally)
API_BASE_URL = "http://127.0.0.1:8000"  
DB_FILE = "/home/sriyaraomuthyala/bootcamp-sriyamuthyala/Persistent_Queue_System/queue.db"
LOG_FILE = "/home/sriyaraomuthyala/bootcamp-sriyamuthyala/Persistent_Queue_System/output.log"

#  Streamlit Page Config
st.set_page_config(page_title="Persistent Queue Dashboard", layout="wide")

#  Dashboard Header
st.title("📊 Persistent Queue System")
st.write("Monitor and manage job queue in real-time.")

#  Function to Connect to SQLite
def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

# Fetch Job Counts
def get_job_counts():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT status, COUNT(*) FROM queue GROUP BY status")
    job_counts = dict(cursor.fetchall())
    conn.close()
    return job_counts

job_counts = get_job_counts()

#  Show Job Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("🟡 Pending Jobs", job_counts.get("pending", 0))
col2.metric("🔵 Processing Jobs", job_counts.get("processing", 0))
col3.metric("✅ Completed Jobs", job_counts.get("completed", 0))
col4.metric("❌ Failed Jobs", job_counts.get("failed", 0))

#  Live Job Queue Table (Show More Details)
st.subheader("📜 Job Queue Overview")
conn = get_db_connection()
df = pd.read_sql("SELECT job_id, job_data, status, created_at FROM queue ORDER BY created_at DESC", conn)
st.dataframe(df)
conn.close()

# Add a New Job
st.subheader("➕ Add a New Job to Queue")
new_job = st.text_input("Enter Job Data", placeholder="Example: Process dataset.csv")
if st.button("Submit Job"):
    if new_job.strip():
        try:
            response = requests.post(f"{API_BASE_URL}/enqueue", json={"job_data": new_job})
            if response.status_code == 200:
                st.success("✅ Job added successfully!")
            else:
                st.error(f"❌ Failed to add job: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Request failed: {e}")
    else:
        st.warning("⚠️ Job data cannot be empty!")

#  Resubmit Failed & Stuck Jobs
st.subheader("🔄 Admin Actions")
if st.button("Resubmit Failed Jobs"):
    try:
        response = requests.get(f"{API_BASE_URL}/admin/resubmit")
        if response.status_code == 200:
            st.success("✅ Resubmitted all failed and stuck jobs!")
        else:
            st.error(f"❌ Error resubmitting jobs: {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Request failed: {e}")

# Show System Logs
st.subheader("📑 System Logs")
try:
    with open(LOG_FILE, "r") as f:
        logs = f.readlines()
    st.text_area("Log Output", "\n".join(logs[-20:]), height=200)
except FileNotFoundError:
    st.error("❌ Log file not found!")
