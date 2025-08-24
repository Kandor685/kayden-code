# =========================================
# =========================================
# SIMPLE FUNCTION AND PROCEDURE TASKS
# =========================================

# Task 1: Simple Function Declaration
# Write a simple function named "greet" that takes no parameters and prints "Hello, world!" when called.

def greet():
    print("Hello World!")
greet()

# Task 2: Function with Parameters
# Write a function named "greet_person" that takes a name as a parameter and prints "Hello, <name>!" when called.

def greet_person(name):
    print(f"Hello, {name}, it's very nice to meet you!")

User_name = input("What's your name? ")
greet_person(User_name)

# Task 3: Function with Return Value
# Write a function named "add" that takes two numbers as parameters, adds them, and returns the result.

def add(num1, num2):
    return num1 + num2

print(add(1, 2))

# Task 4: Function with Default Parameter
# Write a function named "greet_language" that takes a name and a language (default to "English").
# If called with only the name, it should greet the person in English. If called with both name and language,
# it should greet in the specified language.

def greet_language(name, language="English"): 
    if language.lower() == "english": 
        print(f"Hello, {name}!") 
    elif language.lower() == "spanish": 
        print(f"Hola, {name}!") 
    elif language.lower() == "french": 
        print(f"Bonjour, {name}!") 
    else:
        print(f"Hello, {name}! (Sorry, I don't speak {language} well)")
greet_language(language = input("Choose a Language: English, spanish, french: "), name= input("What is your name? "))

# Task 5: Procedure that Modifies Global Variable
# Write a procedure named "increment_counter" that increments a global variable "counter" by 1.

counter = 0

def increment_counter(counter):
    counter = counter + 1

increment_counter(counter)

# Task 6: Procedure without Return
# Write a procedure named "print_square" that takes a number as a parameter, calculates its square, and prints it.

def print_sqaure(num1):
    return num1 * num1
print(print_sqaure(num1 = int(input("Enter a number: "))))

# Task 7: Function that Returns Multiple Values
# Write a function named "calculate" that takes two numbers as input and returns their sum and product.

def calculate (num1, num2):
    return num1 + num2, num1 * num2


print(calculate(num1= int(input("Enter a number: ")), num2= int(input("Enter another number: "))))

# Task 8: Recursive Function
# Write a recursive function named "factorial" that takes an integer n as input and returns its factorial.

import math

def factorial(number1):
    return math.factorial(number1)

print(factorial(number1 = int(input("Enter a number and find it's factorial: "))))

# Task 9: Function with Arbitrary Number of Arguments
# Write a function named "print_names" that takes any number of names as arguments and prints them all.

def print_names(*names):
    for name in names:
        print(name)

print_names("Mark", "Bill", "Sue", "Laura")

# Task 10: Lambda Function
# Write a lambda function that takes two numbers as input and returns their product.

multiply = lambda a,b : a * b

print("Product Using Lambda: ", multiply(2, 3))

# =========================================
# =========================================
# ADVANCED FUNCTION AND PROCEDURE TASKS
# =========================================

# Task 1: Function with Keyword Arguments
# Write a function named "introduce" that takes a name, age, and city as keyword arguments
# and prints an introduction message.


# Task 2: Function with Nested Functions
# Write a function named "outer_function" that defines and calls an inner function "inner_function" inside it.
# "inner_function" should simply print a message.


# Task 3: Function with Decorator
# Write a decorator function named "uppercase_decorator" that modifies a function to return its result in uppercase.
# Apply it to a function named "greet" that returns a greeting message.


# Task 4: Memoization with Recursive Fibonacci
# Write a recursive Fibonacci function that uses memoization to improve performance.


# Task 5: Function with Default and Keyword Arguments Combined
# Write a function named "order_food" that takes a required argument for the main dish and optional keyword arguments
# for sides and drink (with default values). Print the full order.


# Task 6: Function with Variable Length Keyword Arguments (kwargs)
# Write a function named "user_profile" that takes any number of keyword arguments and prints the user information.


# Task 7: Recursive Function for Exponentiation
# Write a recursive function named "power" that calculates x raised to the power y (x^y).


# Task 8: Function as a Parameter to Another Function
# Write a function named "apply_function" that takes another function as an argument and applies it to a number.


# Task 9: Function Returning Another Function
# Write a function named "make_multiplier" that takes a number and returns a function that multiplies its argument by that number.


# Task 10: Higher-Order Function with Map
# Write a higher-order function using `map` that takes a list of numbers and returns a list of their squares.


print("Complete")