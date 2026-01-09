# #Python Basics

# #List
# print(variable[item]) # Access item in the index/position(0 to n)
# print(variable[-item]) # Access counts of item from last index/position back to first index/position
# variable.append(item-value) # Add item-value(string or number) to the end of the list
# variable.insert(item, item-value) # Add item-value(string or number) at specific position/index in the list
# .remove(item-value) # Remove item-value(string or number) from the list
# del variable[item] # Delete item at specific position/index in the list
# variable.pop() # Remove and return the last item in the list
# variable.pop(item) # Remove and return item at specific position/index in the list
# variable.sort() # Sort the list in ascending order
# variable.sort(reverse=True) # Sort the list in descending order
# variable.reverse() # Reverse the order of the list
# len(variable) # Get the number of items in the list
# variable.count(item-value) # Count occurrences of item-value in the list
# variable.index(item-value) # Get the index/position of the first occurrence of item-value in the list
# variable.clear() # Remove all items from the list
# variable.copy() # Create a shallow copy of the list
# variable.extend(another-list) # Add items from another-list to the end of the list
# new_variable = variable[2:4] # Slice the list from index 2 to 3 (4 is excluded)
# new_variable = variable[:3] # Slice the list from start to index 2 (3 is excluded)
# new_variable = variable[2:] # Slice the list from index 2 to the end
# new_variable = variable[-3:] # Slice the last 3 items from the list
# new_variable = variable[:-3] # Slice the list excluding the last 3 items
# new_variable = variable[::2] # Slice the list to get every second item
# new_variable = variable[::-1] # Slice the list to get items in reverse order
# variable1 + variable2 # Concatenate two lists
# variable * n # Repeat the list n times


# Tuples
variable = (1, 2, 3)
variable = ("beans",) # Single item tuple
print(variable[0]) # Access item in the index/position(0 to n)
print(variable[-1]) # Access counts of item from last index/position back to first index/position

# Dictionaries
variable = {"key1": "value1", "key2": "value2"}
print(variable["key1"]) # Access value using key
variable["key3"] = "value3" # Add key-value pair to the dictionary
variable["key1"] = "new_value1" # Update value for existing key
del variable["key2"] # Delete key-value pair using key
variable.pop() # Remove and return an arbitrary key-value pair
variable.pop("key3") # Remove and return value for the specified key
print(variable.keys()) # Get all keys in the dictionary
print(variable.values()) # Get all values in the dictionary
for key, value in variable.items(): # Iterate through key-value pairs
    print(key, value)

# Sets
numbers = {1, 2, 3, 4}, empty_set = set()
numbers.add(5) # Add item to the set
numbers.remove(3) # Remove item from the set
numbers.discard(6) # Remove item if it exists, do nothing if it doesn't
# set1 and set2 Operations: | Union, & Intersection, - Difference, ^ Symmetric Difference