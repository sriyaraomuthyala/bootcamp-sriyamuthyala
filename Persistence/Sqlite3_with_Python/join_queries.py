import sqlite3

def get_products_with_categories():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    query = """
    SELECT products.id, products.name, products.price, categories.category_name
    FROM products
    JOIN product_categories ON products.id = product_categories.product_id
    JOIN categories ON product_categories.category_id = categories.id
    """
    cursor.execute(query)
    
    results = cursor.fetchall()
    for row in results:
        print(row)

    conn.close()

get_products_with_categories()
