### **Persistent Queue System**  
A **fault-tolerant producer-consumer system** with a **persistent queue**, built using **FastAPI, SQLite, and Streamlit**.  
This system ensures jobs **survive restarts**, supports **automatic retries**, and provides a **dashboard for monitoring & administration**.  

---

## **🔹 Features**  
✅ **Persistent queue** (SQLite-based, jobs survive restarts)  
✅ **Multiple producers & consumers** (supports scalability)  
✅ **Supervisor-managed process automation** (auto-restarts on failure)  
✅ **Failure handling & automatic job retries (up to 3 attempts)**  
✅ **Resilient queue system** with **no direct SQLite access from producers/consumers**  
✅ **Admin dashboard** (monitor & manage jobs in real-time)  

---

## **Quick Start Guide**  

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

---

## **🔄 Handling Failures & Retries**  
✅ **Automatic Retry System**  
- If a job **fails**, it is retried **up to 3 times** before being marked as **"failed"**.  
- Consumers **only fetch jobs that have less than 3 attempts** to prevent infinite retries.  

✅ **Automatic Resubmission of Stuck Jobs**  
- If a **consumer crashes** mid-processing, jobs remain in `"processing"`.  
- A **background admin process resets stuck jobs** back to `"pending"`.  
- Admins can **manually resubmit failed jobs** using:  
  ```bash
  poetry run python scripts/admin.py --resubmit
  ```
   **Ensures all jobs are either processed or properly marked as failed.**  

---

## ** Abstraction & Security Updates**  
**-Producers & consumers never interact with SQLite directly.**  
**-All queue operations (enqueue, dequeue, mark done, retries) are handled via `QueueManager`.**  
**-Thread-safe locks prevent race conditions between multiple consumers.**  
**-Producers and consumers only interact via `QueueManager` methods.**  
**-Jobs are processed deterministically, avoiding REST API reliance.**  

---

## **📊 Streamlit Dashboard**  
The **Streamlit dashboard** provides:  
**-Live job queue table** (Pending, Processing, Completed, Failed)  
**-Add new jobs via UI**  
**-Resubmit failed jobs**  
**-Monitor system logs**  

 **Run the dashboard:**  
```bash
poetry run streamlit run ops/dashboard.py --server.port 8501 --server.address 0.0.0.0
```
Then visit:  
```
http://YOUR_VM_EXTERNAL_IP:8501
```  
