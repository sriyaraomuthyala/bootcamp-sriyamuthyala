### **Persistent Queue System**
A **fault-tolerant producer-consumer system** with a **persistent queue**, built using **FastAPI, SQLite, and Streamlit**.  
This system ensures jobs **survive restarts**, supports **automatic retries**, and provides a **dashboard for monitoring & administration**.

---

## **🔹 Features**
✅ **Persistent queue** (SQLite-based, jobs survive restarts)  
✅ **Multiple producers & consumers** (supports scalability)  
✅ **Supervisor-managed process automation** (auto-restarts on failure)  
✅ **Failure handling & automatic job resubmission**  
✅ **Admin dashboard** (monitor & manage jobs in real-time)  

---

## ** Quick Start Guide**
### **1️⃣ Install Dependencies**
```bash
poetry install
```

### **2️⃣ Initialize Database**
```bash
poetry run python scripts/setup_db.py
```

### **3️⃣ Start All Services Using Supervisor**
```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start all
```
✅ This ensures that **FastAPI, producers, and consumers run automatically**.  

### **4️⃣ Open the Streamlit Dashboard**
```bash
http://YOUR_VM_EXTERNAL_IP:8501
```
✅ **Monitor queue, submit jobs, and resubmit failed tasks!**  

---

## **🛠 API Endpoints**
| Method | Endpoint | Description |
|--------|---------|------------|
| `POST` | `/enqueue/` | **Add a job to the queue** |
| `GET`  | `/dequeue/` | **Consumer fetches a job** |
| `POST` | `/mark_done/{job_id}` | **Mark a job as completed** |
| `GET`  | `/admin/resubmit` | **Resubmits all failed jobs** |

💡 **Example: Submit a Job Using `curl`**
```bash
curl -X 'POST' 'http://127.0.0.1:8000/enqueue/' \
     -H 'Content-Type: application/json' \
     -d '{"job_data": "Process dataset.csv"}'
```

✅ **Response:**
```json
{
    "message": "Job enqueued",
    "job_id": "b123e4567-e89b-12d3-a456-426614174000"
}
```

---

## **🔄 Handling Failures**
- If a **consumer crashes** mid-processing, the job remains in **"processing"**.
- A background **admin process resets stuck jobs** to `"pending"`.
- Admins can manually **resubmit failed jobs** using:
  ```bash
  poetry run python scripts/admin.py --resubmit
  ```
  ✅ **Now, failed jobs get reprocessed!**

---

## **📊 Streamlit Dashboard**
The **Streamlit dashboard** provides:  
✅ **Live job queue table** (Pending, Processing, Completed, Failed)  
✅ **Add new jobs via UI**  
✅ **Resubmit failed jobs**  
✅ **Monitor system logs**  

💡 **Run the dashboard:**
```bash
poetry run streamlit run ops/dashboard.py --server.port 8501 --server.address 0.0.0.0
```
Then visit:
```
http://YOUR_VM_EXTERNAL_IP:8501
```
