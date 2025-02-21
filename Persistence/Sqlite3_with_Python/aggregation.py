import sqlite3

def get_total_stock_value():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(price) FROM products")
    total_value = cursor.fetchone()[0]

    print(f"Total stock value: ${total_value}")

    conn.close()

get_total_stock_value()
