# ChatGPT link: https://chatgpt.com/c/4747e234-0cf3-4260-8dca-1e09d6eff249

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __repr__(self):
        return f"{self.name}, ${self.price:.2f}, {self.quantity} in stock"

    def update_quantity(self, quantity): # updates quantity of item
        self.quantity += quantity
        print(f"New quantity is: {self.quantity}")

    def calculate_total_value(self): # calculates the total value of the item (price * quantity)
        return self.price * self.quantity

class Inventory:
    def __init__(self):
        self.items = []
    
    def __repr__(self):
        inventory_list = ', '.join([str(item) for item in self.items])
        return f"Inventory: [{inventory_list}]"

    def add_item(self, item): # add a new item to the inventory
        self.items.append(item)

    def remove_item(self, item_name): # remove an item from inventory by name
        for item in self.items:
            if item_name == item.name:
                self.items.remove(item)
                print(f"{item_name} removed from inventory.")
                return
        print(f"Item '{item_name}' not found in inventory.")

    def get_total_inventory_value(self): # calculate the total value of all items in the inventory
        inventory_value = 0
        for item in self.items:
            inventory_value += item.calculate_total_value()
        print(f"Inventory value: ${inventory_value:.2f}")
        return inventory_value

# Testing implementation
item1 = Item('Apple', 0.5, 100)
item2 = Item('Banana', 0.3, 150)
item3 = Item('Orange', 0.8, 80)

inventory = Inventory()
inventory.add_item(item1)
inventory.add_item(item2)
inventory.add_item(item3)

print(inventory)

inventory.remove_item('Banana')

print(inventory)