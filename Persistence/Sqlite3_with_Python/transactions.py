import sqlite3

def transaction_example():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    try:
        cursor.execute("BEGIN TRANSACTION")

        cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", ("Monitor", 199.99))
        cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", ("Keyboard", 49.99))

        # Uncomment to simulate failure
        # raise Exception("Something went wrong!")

        conn.commit()
        print("Transaction Successful!")

    except Exception as e:
        conn.rollback()
        print("Transaction Failed! Rolling back...")
        print(e)

    finally:
        conn.close()

def transaction_handling():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    try:
        cursor.execute("BEGIN TRANSACTION")

        cursor.execute("INSERT INTO products (name, price) VALUES ('USB Cable', 10.99)")
        cursor.execute("INSERT INTO products (name, price) VALUES ('Mouse Pad', 15.99)")

        conn.commit()
        print("Transaction committed successfully!")

    except sqlite3.Error as e:
        conn.rollback()
        print(f"Transaction failed: {e}")

    finally:
        conn.close()

transaction_handling()

transaction_example()
