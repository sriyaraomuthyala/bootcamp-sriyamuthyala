from fastapi import FastAPI
import sqlite3

app = FastAPI()

def connect_db():
    return sqlite3.connect("store.db")

@app.get("/products")
def get_products():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return {"products": products}

@app.post("/products")
def add_product(name: str, price: float):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    conn.close()
    return {"message": "Product added successfully"}
