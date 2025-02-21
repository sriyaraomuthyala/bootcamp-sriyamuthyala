from product_class import Product

store = Product()
products = store.get_products()
for product in products:
    print(product)

store.close()
