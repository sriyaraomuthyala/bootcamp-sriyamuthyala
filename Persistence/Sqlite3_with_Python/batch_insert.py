import sqlite3

def batch_insert(products):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)

    conn.commit()
    conn.close()
    print("Batch insertion successful!")

# Example usage
batch_insert([
    ("Mouse", 25.99),
    ("Charger", 19.99),
    ("Speaker", 79.99)
])
