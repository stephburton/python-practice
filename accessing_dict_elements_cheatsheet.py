# Accessing Dictionary Elements

'''
1. self.products:

- This accesses the entire dictionary.
- Use this when you need to perform operations that involve both keys and values or when you need the dictionary as a whole.

2. self.products.keys():

- This accesses only the keys of the dictionary.
- Use this when you are only interested in the keys, for example, when you want to check if a particular key exists in the dictionary.

3. self.products.values():

- This accesses only the values of the dictionary.
- Use this when you are only interested in the values, for example, when you want to iterate over all the values without caring about their keys.

4. self.products.items():

- This accesses both the keys and values as tuples.
- Use this when you need both the key and value, for example, when iterating over the dictionary to access each key-value pair.
'''
# Examples

'''
1. Accessing Entire Dictionary:

- Use self.products when you want to print the entire dictionary or pass it to another function.
'''
print(self.products)  # Prints the entire dictionary

'''
2. Accessing Keys:

- Use self.products.keys() when you want to check for the existence of a key or iterate over keys.
'''
if product_name in self.products.keys():
    print(f"{product_name} is in the inventory.")

'''
3. Accessing Values:

- Use self.products.values() when you want to iterate over the values (e.g., Product objects) without needing the keys.
'''
for product in self.products.values():
    print(product)  # Prints each Product object

'''
4. Accessing Items:

- Use self.products.items() when you need both keys and values, for example, to print the key-value pairs.
'''
for name, product in self.products.items():
    print(f"Key: {name}, Value: {product}")

# When to Use Each Method

'''
1. Iterating Over Values:

- When you only need to work with the Product objects without their names, use self.products.values().
'''
for product in self.products.values():
    print(product)

'''
2. Iterating Over Keys:

- When you only need the product names, use self.products.keys().
'''
for name in self.products.keys():
    print(name)

'''
3. Iterating Over Key-Value Pairs:

- When you need both the product names and Product objects, use self.products.items().
'''
for name, product in self.products.items():
    print(f"{name}: {product}")

# Examples in Context
'''
For printing the inventory, you want to print each Product object, so you use self.products.values():
'''
def print_inventory(self):
    for product in self.products.values():
        print(product)

'''
If you needed to print both the name and the Product object, you would use self.products.items():
'''
def print_inventory(self):
    for name, product in self.products.items():
        print(f"Product Name: {name}, Details: {product}")

# Summary
'''
- Use self.products for the entire dictionary.
- Use self.products.keys() for just the keys.
- Use self.products.values() for just the values.
- Use self.products.items() for key-value pairs.
'''