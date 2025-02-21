import sqlite3

def transfer_funds(sender_id, receiver_id, amount):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    try:
        cursor.execute("BEGIN TRANSACTION")

        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (amount, sender_id))
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, receiver_id))

        conn.commit()
        print("Transaction successful!")

    except sqlite3.Error as e:
        conn.rollback()
        print(f"Transaction failed: {e}")

    finally:
        conn.close()

transfer_funds(1, 2, 100)
