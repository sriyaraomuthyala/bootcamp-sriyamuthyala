import sqlite3

def update_inventory(product_id, quantity):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    try:
        cursor.execute("BEGIN TRANSACTION")

        cursor.execute("UPDATE products SET price = price * 1.05 WHERE id = ?", (product_id,))
        cursor.execute("INSERT INTO inventory_log (product_id, quantity) VALUES (?, ?)", (product_id, quantity))

        conn.commit()
        print("Inventory update successful!")

    except sqlite3.Error as e:
        conn.rollback()
        print(f"Inventory update failed: {e}")

    finally:
        conn.close()

update_inventory(1, 5)
