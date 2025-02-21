import sqlite3

class Product:
    def __init__(self, db_name="store.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_product(self, name, price):
    if not isinstance(name, str) or not isinstance(price, (int, float)) or price <= 0:
        print("Invalid data: Name must be a string and price must be a positive number.")
        return
    
        self.cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        self.conn.commit()


    def get_products(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

    def update_product(self, product_id, new_price):
        self.cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        self.conn.commit()

    def search_product(self, name_fragment):
        self.cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + name_fragment + '%',))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
