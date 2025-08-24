# =========================================
# =========================================
# SIMPLE DICTIONARY TASKS
# =========================================

# Task 1: Create a Dictionary
# Create a dictionary with the following key-value pairs:
# 'name': 'John', 'age': 30, 'city': 'New York'
# Print the dictionary.
# ---

thisdict = {
    "name" : "John",
    "age" : 30,
    "city" : "New York"
}
print(thisdict)

# Task 2: Access Dictionary Values
# Access and print the value associated with the key 'age' from the dictionary created in Task 1.
# ---

a = thisdict.get("age")
print (a)

# Task 3: Add New Key-Value Pair
# Add a new key-value pair 'occupation': 'Engineer' to the dictionary.
# Print the updated dictionary.
# ---

thisdict["occupation"] = "Engineer"
print(thisdict)

# Task 4: Update a Value
# Update the value associated with the key 'city' to 'San Francisco'.
# Print the updated dictionary.
# ---

thisdict.update({"city" : "San Francisco"})
print (thisdict)

# Task 5: Delete a Key-Value Pair
# Delete the key-value pair with the key 'age' from the dictionary.
# Print the dictionary.
# ---

thisdict.pop("age")
print(thisdict)
# Task 6: Check if Key Exists
# Check if the key 'name' exists in the dictionary. Print 'Key exists' if it does, otherwise print 'Key does not exist'.
# ---

if "name" in thisdict:
    print ("Key exists")
else: 
    Print("Key does not exist")

# Task 7: Iterate Over Keys
# Iterate over the keys of the dictionary and print each key.
# ---

for x in thisdict.keys():
  print(x)

# Task 8: Iterate Over Values
# Iterate over the values of the dictionary and print each value.
# ---

for x in thisdict.values():
    print(x)

# Task 9: Iterate Over Key-Value Pairs
# Iterate over the dictionary items and print each key-value pair.
# ---
for x, y in thisdict.items():
    print (x, "-", y)
# Task 10: Dictionary Length
# Print the number of key-value pairs in the dictionary.
# ---

b = len (thisdict)
print (b)

# =========================================
# =========================================
# ADVANCED DICTIONARY TASKS
# =========================================

# Task 11: Dictionary Comprehension
# Use a dictionary comprehension to create a dictionary where the keys are numbers from 1 to 5, and the values are their squares.
# Print the dictionary.
# ---



# Task 12: Nested Dictionaries
# Create a nested dictionary to represent a student with name, age, and subjects (where subjects is another dictionary with subject names as keys and grades as values).
# Print the nested dictionary.
# ---

nestdict = {
    "student name" : "Bob",
    "age" : 16,
    "subjects with grades" : {
        "English" : "B",
        "Maths" : "F",
        "Science" : "C",
        "Computer Science" : "B+",
        "Geography" : "C"
    }
}
print (nestdict)
# Task 13: Merge Dictionaries
# Merge two dictionaries into one. Dictionary 1: {'a': 1, 'b': 2} and Dictionary 2: {'c': 3, 'd': 4}.
# Print the merged dictionary.
# ---

diction1 = {
    "a" : 1,
    "b" : 2
}

diction2 = {
    "c" : 3,
    "d" : 4
}

diction1.update (diction2)

print (diction1)

# Task 14: Dictionary from List of Tuples
# Convert a list of tuples [('apple', 1), ('banana', 2), ('cherry', 3)] into a dictionary.
# Print the dictionary.
# ---

# Task 15: Dictionary with Default Values
# Create a dictionary with default values for keys that do not exist using collections.defaultdict.
# For example, initialize a dictionary with integer default values and add some key-value pairs.
# Print the dictionary.
# ---

# Task 16: Update Dictionary with Another Dictionary
# Use the `update` method to add or update key-value pairs from another dictionary. 
# Dictionary 1: {'name': 'Alice', 'age': 25}, Dictionary 2: {'age': 30, 'city': 'Boston'}.
# Print the updated dictionary.
# ---

# Task 17: Filter Dictionary
# Given a dictionary with numerical values, filter out and create a new dictionary with only items where the value is greater than 10.
# Dictionary: {'a': 5, 'b': 15, 'c': 20}.
# Print the filtered dictionary.
# ---

# Task 18: Dictionary with List Values
# Create a dictionary where the values are lists. For example, {'fruits': ['apple', 'banana'], 'vegetables': ['carrot', 'spinach']}.
# Print the dictionary, and then add a new item to the 'fruits' list.
# ---

# Task 19: Dictionary Operations with Functions
# Write a function that takes a dictionary and a key, and returns the value associated with that key.
# If the key does not exist, return a default value of 'Not found'.
# ---

# Task 20: Dictionary Sorting
# Given a dictionary with numerical values, sort the dictionary by its values in descending order.
# Print the sorted dictionary.
# ---
