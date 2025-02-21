import sqlite3
import csv

def export_to_csv():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    with open("products.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Price"])
        writer.writerows(products)

    conn.close()
    print("Data exported to products.csv")

export_to_csv()
