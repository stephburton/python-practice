# A typical paired-programming interview question found online. I asked ChatGPT to guide me through it.
# ChatGPT Link: https://chatgpt.com/c/840b098a-636a-4c75-ab87-3d361d5b8d3d

# def find_fulfilling_cities(inventory, order_request):
#     fulfilling_cities = []
    
#     for city, city_inventory in inventory.items():
#         can_fulfill = True  # Assume the city can fulfill the order
        
#         for item, quantity in order_request.items():
#             if city_inventory.get(item, 0) < quantity:
#                 can_fulfill = False  # The city cannot fulfill the order
#                 break
        
#         if can_fulfill:
#             fulfilling_cities.append(city)
    
#     return fulfilling_cities

# inventory = {
#     'Toronto': {'apples': 10, 'bananas': 5},
#     'Vancouver': {'apples': 3, 'bananas': 10},
#     'Montreal': {'apples': 8, 'bananas': 8}
# }

# order_request = {'apples': 5, 'bananas': 5}

# result = find_fulfilling_cities(inventory, order_request)
# print(result)  # Expected output: ['Toronto', 'Montreal']

# More practice on breaking down verbal coding problems:

# "Given a list of numbers, find the maximum number"
# input -> a list of numbers
# output -> the maximum number of the list
# function -> find the max number

def find_max_number(number_list):
    max_number = 0
    for number in number_list:
        if number > max_number:
            max_number = number
    return max_number

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(find_max_number(numbers))