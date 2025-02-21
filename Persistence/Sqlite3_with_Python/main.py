from product_class import Product

store = Product()
store.add_product("Headphones", 149.99)
print(store.get_products())
store.update_product(1, 129.99)
store.delete_product(3)
store.close()
