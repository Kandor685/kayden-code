# =========================================
# =========================================
# BASIC PYTHON FUNCTIONS (PYTHON STANDARD LIBRARY) TASKS
# =========================================

# Task 1: String Functions
# Write a function that takes a string as input and uses built-in functions like `len`, `str.upper`, and `str.count` to manipulate and display information about the string.
# ---

mystring = "hello world"

print (mystring)

newstring = mystring.upper()

print (newstring)

# Task 2: List Functions
# Write a function that takes a list of integers as input and uses built-in functions like `sum`, `max`, and `min` to perform calculations and display results.
# ---

#create the list
intlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#define the variable to print the sum of the list
total = sum(intlist)

print(f"Total of List: {total}")


#define the variable to print the highest number in the list
Highest = max(intlist)

print(f"Highest number in list: {Highest}")

#define the variabe to print the lowest number in the list
lowest = min(intlist)

print(f"Lowest number in list: {lowest}")

# Task 3: Date and Time Functions
# Write a function that uses the `datetime.datetime.now` function to display the current date and time.
# ---

import datetime

current = datetime.datetime.now()

print(current)

# Task 4: File Functions
# Write a function that uses the `open`, `read`, and `close` functions to read and display the contents of a text file.
# ---

file = open("demofile.txt", "r")

print(file.read())

("demofile.txt", "c")

# Task 5: Dictionary Functions
# Write a function that uses dictionary functions like `dict.keys`, `dict.values`, and `dict.items` to manipulate and display information about a dictionary.
# ---

exam_results = {
    "Alice" : 86, 
    "Bob" : 67,
    "Charlie" : 75
}

dictionary_keys = exam_results.keys()

exam_results["Dominic"] = 73

print (dictionary_keys)

dictionary_values = exam_results.values()

print(dictionary_values)

dictionary_items = exam_results.items()

print(dictionary_items)

# Task 6: List Comprehension
# Write a function that uses list comprehension to generate a list of square numbers from 1 to 10.
# ---

Squares = [x**2 for x in range(1, 11)]

print(Squares)

# Task 7: Random Number Generation
# Write a function that uses the `random.randint` function to generate and return a random number between 1 and 100.
# ---

import random

rand_num = random.randint(1, 100)

print(rand_num)

# Task 8: Exception Handling
# Write a function that uses a `try...except` block to handle division by zero and display an error message.
# ---

# try:
#     num1 / 0
# except:
#     print("ERROR: nothing can be divided by 0")

# Task 9: String Formatting
# Write a function that uses f-strings to format and display a message with variables.
# ---

variable1 = 1247289347124 
variable2 = -12389923478192

print(f"{variable1} is greater than {variable2}")

# Task 10: URL Parsing
# Write a function that uses the `urllib.parse.urlparse` function to parse a URL and display its components.
# ---

#???

# =========================================
# =========================================
# ADVANCED PYTHON FUNCTIONS (PYTHON STANDARD LIBRARY) TASKS
# =========================================

# Task 11: CSV File Processing
# Write a function that uses the `csv.reader` function to read and display data from a CSV file.
# ---

# Task 12: Regular Expressions
# Write a function that uses the `re.search` function to search for a specific pattern (e.g., an email address) in a given string and display the result.
# ---

# Task 13: JSON Data Manipulation
# Write a function that uses the `json.loads` and `json.dumps` functions to load and manipulate JSON data.
# ---

# Task 14: Sorting Custom Objects
# Create a class representing custom objects (e.g., Product with name and price).
# Write a function that uses the `sorted` function with a custom key function to sort a list of these objects based on a specific attribute (e.g., price).
# ---

# Task 15: Database Connection
# Write a function that uses the `sqlite3.connect` function to connect to an SQLite database, execute a query, and display the results.
# ---

# Task 16: Web Scraping
# Write a function that uses web scraping libraries like `requests` and `BeautifulSoup` to scrape data (e.g., headlines from a news website) and display the results.
# ---

# Task 17: Multithreading
# Write a function that uses the `threading.Thread` class to create multiple threads, each performing a specific task, and display the results.
# ---

# Task 18: File Compression
# Write a function that uses the `gzip` library to compress a large text file and save it as a compressed file.
# ---

# Task 19: API Integration
# Write a function that uses the `requests.get` function to fetch data from a public API (e.g., weather forecast) and display the results.
# ---

# Task 20: Data Analysis
# Write a function that uses the `pandas` library to load and analyze a dataset, performing operations like filtering, grouping, and displaying summary statistics.
# ---
