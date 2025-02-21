from product_class import Product

store = Product()
results = store.search_product("Laptop")
for product in results:
    print(product)

store.close()
