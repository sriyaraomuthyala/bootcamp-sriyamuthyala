import sqlite3

def update_product_category(product_id, category_id):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    try:
        cursor.execute("BEGIN TRANSACTION")

        cursor.execute("UPDATE products SET price = price * 1.1 WHERE id = ?", (product_id,))
        cursor.execute("INSERT INTO product_categories (product_id, category_id) VALUES (?, ?)", (product_id, category_id))

        conn.commit()
        print("Update successful!")

    except sqlite3.Error as e:
        conn.rollback()
        print(f"Transaction failed: {e}")

    finally:
        conn.close()

update_product_category(1, 2)
