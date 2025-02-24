import streamlit as st
import sqlite3

st.title("Persistent Queue Status")

conn = sqlite3.connect("queue.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM queue")
jobs = cursor.fetchall()

for job in jobs:
    st.write(f"Job ID: {job[0]}, Status: {job[2]}")
