# Python Dictionary Cheatsheet

# Basic Dictionary Structure
# A dictionary is a collection of key-value pairs.

my_dict = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
}

# Accessing Values
# To access a value, use the key inside square brackets or the get() method.

value = my_dict['key1']  # Using square brackets
value = my_dict.get('key1')  # Using get() method

# Adding / Updating Entries
# To add or update an entry, simply assign a value to a key

my_dict['key4'] = 'value4'  # Adds a new key-value pair
my_dict['key1'] = 'new_value1'  # Updates the value for key1

# Removing Entries
# To remove a key-value pair, use the del statement or the pop() method.

del my_dict['key2']  # Removes key2
value = my_dict.pop('key3')  # Removes key3 and returns its value

# Checking for Existence
# To check if a key exists in the dictionary, use the in keyword.

if 'key1' in my_dict:
    print("key1 exists in the dictionary")

# Iterating Over Dictionaries
# You can iterate over keys, values, or key-value pairs.

# Iterating over keys
for key in my_dict:
    print(key)

# Iterating over values
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Using Dictionaries in Functions
# 1. Passing a dictionary to a function:
def print_dict(d):
    for key, value in d.items():
        print(f"{key}: {value}")

my_dict = {'a': 1, 'b': 2, 'c': 3}
print_dict(my_dict)
# 2. Modifying a dictionary within a function:
def update_dict(d, key, value):
    d[key] = value

my_dict = {'a': 1, 'b': 2}
update_dict(my_dict, 'c', 3)
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
# 3. Returning a dictionary from a function:
def create_dict(keys, values):
    return dict(zip(keys, values))

keys = ['a', 'b', 'c']
values = [1, 2, 3]
new_dict = create_dict(keys, values)
print(new_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
# 4. Accessing dictionary values safely:
def get_value(d, key):
    return d.get(key, 'Key not found')

my_dict = {'a': 1, 'b': 2}
print(get_value(my_dict, 'a'))  # Output: 1
print(get_value(my_dict, 'c'))  # Output: Key not found

# Example Usage in a More Complex Function
def summarize_activities(logs):
    activity_count = {}
    for log in logs:
        activity = log.get('Activity')
        if activity in activity_count:
            activity_count[activity] += 1
        else:
            activity_count[activity] = 1
    return activity_count

logs = [
    {'Time': '10:00', 'UserID': '123', 'Activity': 'Login'},
    {'Time': '10:05', 'UserID': '124', 'Activity': 'Logout'},
    {'Time': '10:10', 'UserID': '123', 'Activity': 'Login'},
]

print(summarize_activities(logs))
# Output: {'Login': 2, 'Logout': 1}