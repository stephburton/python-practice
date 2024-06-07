# For Loop
"""
Purpose: Iterate over a sequence (like a list, tuple, dictionary, set, or string).
"""
# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop through a string
for letter in "banana":
    print(letter)

# Loop through a dictionary
user_activities = {'2023-06-07': 'coding', '2023-06-08': 'meeting', '2023-06-09': 'reviewing'}
for date, activity in user_activities.items():
    print(f"On {date}, activity: {activity}")

# Using range
for i in range(5):
    print(i)

# While Loop
'''
Purpose: Repeat as long as a condition is true.
'''
count = 0
while count < 5:
    print(count)
    count += 1

# Break and Continue
'''
Purpose: Control the flow of loops.
'''
# Break example
for num in range(10):
    if num == 5:
        break
    print(num)

# Continue example
for num in range(10):
    if num == 5:
        continue
    print(num)

# Nested Loops
'''
Purpose: Loop inside another loop.
'''
# Nested for loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for adjective in adj:
    for fruit in fruits:
        print(adjective, fruit)

# Nested while loop
i = 1
while i < 4:
    j = 1
    while j < 4:
        print(i, j)
        j += 1
    i += 1

# Looping with Else
'''
Purpose: Run a block of code once when the loop condition no longer holds.
'''
# For loop with else
for num in range(3):
    print(num)
else:
    print("Loop finished")

# While loop with else
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Loop finished")

# Iterating with Enumerate
'''
Purpose: Get index and value from a list.
'''
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Looping over a List with List Comprehensions
'''
Purpose: Create a new list by applying an expression to each item in an existing list.
'''
# Simple list comprehension
squares = [x**2 for x in range(10)]
print(squares)

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)