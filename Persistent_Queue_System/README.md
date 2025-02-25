# Persistent Queue System

## Overview
This is a **producer-consumer system** with a **persistent queue** using FastAPI, SQLite, and Streamlit.  
It supports multiple producers and consumers, ensures **jobs survive restarts**, and provides an **admin panel**.

## Features
✅ Multiple producers & consumers  
✅ Persistent queue (SQLite)  
✅ Fault-tolerant job processing  
✅ Supervisor-based process management  
✅ Streamlit dashboard for monitoring  

## Setup Instructions

### 1️⃣ Install Dependencies
```bash
poetry install

##Initialize Database
poetry run python scripts/setup_db.py

###Start Services Using Supervisor
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start all

###Open Streamlit Dashboard
http://YOUR_VM_EXTERNAL_IP:8501




