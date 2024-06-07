# ChatGPT Link: https://chatgpt.com/c/1bbe8ac9-47cf-4d85-b223-3cb4933caa3c

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)
    
    def __str__(self):
        return f"'{self.name}', ${self.price:.2f}"
    
class Inventory:
    def __init__(self):
        self.products = {}
    
    def __str__(self):
        return '\n'.join([str(product) for product in self.products.values()])

    def add_product(self, product): # add a product to the inventory
        self.products[product.name] = product
        print(f"'{product.name}' added to inventory.")

    def update_price(self, product_name, new_price): # update the price of an existing product
        if product_name in self.products:
            product = self.products[product_name]
            product.price = new_price
            print(f"Price updated for '{product.name}'.")
        else:
            print("Product not found.")

    def remove_product(self, product_name): # remove a product from the inventory
        if product_name in self.products:
            del self.products[product_name]
            print(f"'{product_name}' removed.")
        else:
            print("Product not found.")

    def print_inventory(self): # print all products in the inventory in a formatted manner
        for product in self.products.values():
            print(product)


inventory = Inventory()

inventory.add_product(Product("hat", 10))
inventory.add_product(Product("t-shirt", 25))
inventory.add_product(Product("nice pants", 50))

inventory.update_price("hat", 12)

inventory.remove_product("t-shirt")

inventory.print_inventory()