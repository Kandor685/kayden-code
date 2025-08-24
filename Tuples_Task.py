# =========================================
# =========================================
# SIMPLE TASKS: WORKING WITH TUPLES
# =========================================

# Task 1: Create a Tuple
# Create a tuple called "fruits" containing 'apple', 'banana', 'cherry'.
# Print the tuple.
# ---

fruits = ("apple", "banana", "cherry")
print(fruits)
print("##################################################")

# Task 2: Access Tuple Elements
# Write a program that accesses and prints the second item in the tuple "fruits".
# ---

print(fruits[1])
print("##################################################")

# Task 3: Unpack a Tuple
# Unpack the tuple "fruits" into three variables and print them.
# ---

(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
print("##################################################")

# Task 4: Check Item in Tuple
# Write a program that checks if 'banana' is in the tuple "fruits" and prints the result.
# ---

if "banana" in fruits:
    print ("There is bananas!")
else:
    print("There is not bananas!")
print("##################################################")

# Task 5: Iterate Through a Tuple
# Write a program that uses a for loop to iterate through the tuple "fruits" and prints each item.
# ---

for x in fruits:
    print(x)
print("##################################################")

# Task 6: Concatenate Tuples
# Write a program that concatenates two tuples: 
# ('apple', 'banana', 'cherry') and ('kiwi', 'melon') into a new tuple and prints it.
# ---

fruits2= ("kiwi", "melon")
fruits = fruits + fruits2
print(fruits)
print("##################################################")

# Task 7: Tuple Length
# Write a program that prints the length of the tuple "fruits".
# ---
print(len(fruits))
print("##################################################")

# Task 8: Tuple Indexing
# Write a program that finds and prints the index of 'cherry' in the tuple "fruits".
# ---

index = fruits.index("cherry")
print(index)
print("##################################################")

# Task 9: Tuple Slicing
# Write a program that slices the first two items from the tuple "fruits" and prints the result.
# ---

print(fruits[0:2])
print("##################################################")

# Task 10: Convert Tuple to List
# Write a program that converts the tuple "fruits" into a list, adds 'grape' to the list,
# and then converts it back into a tuple. Print the final tuple.
# ---

fruitlist = list(fruits)
fruitlist.append("grape")
fruits = tuple(fruitlist)
print(fruits)
print("##################################################")

# =========================================
# =========================================
# ADVANCED TASKS: WORKING WITH TUPLES
# =========================================

# Task 11: Nested Tuples
# Write a program that creates a nested tuple containing two tuples:
# ('apple', 'banana', 'cherry') and ('kiwi', 'melon', 'grape').
# Access the second item of the second tuple and print it.
# ---

nestedfruits = (("apple", "banana", "cherry"), ("kiwi", "melon", "grape"))
print(nestedfruits[1][1])
print("##################################################")

# Task 12: Tuple Comprehension Simulation
# Tuples do not have comprehensions. However, write a program that uses a list comprehension
# to generate a list of squares from 1 to 10 and then converts the list into a tuple.
# ---

squares = ("1", "4", "9", "16", "25", "36", "49", "64", "81", "100")
newsquares = []

for x in squares:
    if squares in x:
        newsquares.append(x)
print(newsquares)
print("##################################################")

# Task 13: Tuple Packing and Unpacking with Multiple Return Values
# Write a function called "calculate" that takes two numbers, adds and multiplies them,
# and returns the results as a tuple. Unpack the tuple into two variables and print them.
# ---

# Task 14: Using Tuples as Dictionary Keys
# Write a program that creates a dictionary with tuples as keys and numbers as values.
# Use the tuple ('apple', 'banana') as a key and assign it a value of 5.
# Print the dictionary.
# ---

# Task 15: Immutable Tuples with Mutable Elements
# Write a program that creates a tuple with a list as one of its elements. 
# Modify the list inside the tuple and print the updated tuple.
# ---

# Task 16: Tuple Sorting by Element
# Write a program that creates a list of tuples, where each tuple contains a fruit name and its quantity.
# Sort the list by the fruit quantity (second item in each tuple) and print the sorted list.
# ---

# Task 17: Nested Tuple Unpacking
# Write a program that creates a nested tuple of coordinates: ((1, 2), (3, 4), (5, 6)).
# Unpack the coordinates into variables and print them.
# ---

# Task 18: Tuple with Functions
# Write a program that stores multiple functions (add, subtract, multiply, divide) inside a tuple.
# Call each function from the tuple using two numbers and print the result.
# ---

# Task 19: Count and Index Methods
# Write a program that creates a tuple with repeated items (e.g., 'apple', 'banana', 'apple', 'cherry').
# Use the count() method to find how many times 'apple' appears in the tuple.
# Use the index() method to find the first occurrence of 'cherry'.
# ---

# Task 20: Zipping and Unzipping Tuples
# Write a program that zips two tuples: ('apple', 'banana', 'cherry') and ('red', 'yellow', 'red').
# Print the zipped tuple, and then unzip it back into two separate tuples.
# ---
