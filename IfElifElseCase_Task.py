# =========================================
# =========================================
# SIMPLE CONDITIONAL STATEMENTS TASKS
# =========================================

# Task 1: Simple IF Statement
# Write a program that checks if a number is positive and prints "Positive" if it is.
# ---
# Hint: Use the `if` statement to compare the number with 0.

num = float(input("Enter a number: "))
if num >= 0:
    print(f"{num} is Positive!")
else:
    print(f"{num} is negative!")

# Task 2: IF-ELSE Statement
# Write a program that checks if a number is even or odd, and prints the result.
# ---
# Hint: Use `%` operator to check divisibility by 2.

num1 = int(input("Enter a number "))
if num1 % 2 == 0:
    print(f"{num1} is even!")
else:
    print(f"{num1} is Odd!")
# Task 3: IF-ELIF-ELSE Statement
# Write a program that asks for the user's age and categorizes them into child, teenager, or adult.
# ---
# Hint: Use multiple `elif` statements for the age categories.

age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age > 13 and age < 18:
    print("Teenager")
elif age >= 18:
    print("Adult")
else:
    print("UNKNOWN INPUT")
    
# Task 4: Nested IF Statements
# Write a program that checks if a number is positive, and then checks if it's even or odd.
# ---
# Hint: You can nest `if` statements inside each other.

num = float(input("Enter a number: "))
if num >= 0:
    print(f"{num} is Positive!")
    if num % 2 == 0:
        print(f"{num} is even!")
    else:
        print(f"{num} is Odd!")
else:
    print(f"{num} is negative!")
    if num % 2 == 0:
        print(f"{num} is even!")
    else:
        print(f"{num} is Odd!")
        
# Task 5: Multiple Conditions
# Write a program that checks if a number is divisible by both 3 and 5.
# ---
# Hint: Use the `and` operator in the `if` condition.

num2 = int(input("Enter a number: "))
if num2 % 3 == 0 and num2 % 5 == 0 :
    print(f"{num2} is divisible by 3 and 5!")
else:
    print(f"{num2} is not divisible by 3 and 5!")
    
# Task 6: Check for Presence in List
# Write a program that checks if a given color is present in a list of colors. Print "Found" if it is, else print "Not Found."
# ---
# Hint: Use the `in` operator with an `if` statement.

colours = ["red", "blue", "purple", "green", "pink", "yellow", "orange"]

userColour = input("Enter a colour to see if it's in the list: ")
if userColour in colours:
    print(f"{userColour} is in the list!")
else:
    print(f"{userColour} ins't in the list!")

# Task 7: Case-Like Statement with Dictionary (Simple)
# Write a program that asks the user to enter a number from 1 to 3 and prints a message based on the number (e.g., 1 -> "One", 2 -> "Two").
# ---
# Hint: Use a dictionary to simulate a `switch` statement.

thisdict = {
    1 : "--> One",
    2 : "--> Two",
    3 : "--> Three"
}

user_input = int(input("Enter a number from 1-3: "))

if user_input in thisdict:
    print(thisdict[user_input])
else:
    print("ERROR: Input not in list")    

# Task 8: Logical Operators
# Write a program that checks if a given year is a leap year or not. A leap year is divisible by 4 but not by 100, unless it's also divisible by 400.
# ---
# Hint: Use `and` and `or` operators in the `if` statement.

year = int(input("Enter a year: "))

if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year!")

# Task 9: Conditional Assignment
# Write a program that assigns a value to a variable based on a condition. If a number is greater than 10, assign "High", otherwise "Low".
# ---
# Hint: Use a single-line `if-else` expression (ternary operation).

num_input = float(input("Enter a number: "))

if num_input > 10:
    num_input = "High"
    print(num_input)
else:
    num_input = "Low"
    print(num_input)

# Task 10: Multiple IF Conditions
# Write a program that checks if a number is positive, greater than 50, and even. Print a message only if all conditions are true.
# ---
# Hint: Combine conditions using `and`.

user_num = int(input("Enter a number: "))

if user_num >= 0 and user_num > 50 and user_num % 2 == 0:
    print(f"{user_num} is a positive number, greater than 50 and is even!")
elif user_num <0 and user_num % 2 == 0:
    print(f"{user_num} is a negative number but is still even!")
elif user_num >= 0 and user_num < 50 and user_num % 2 == 0:
    print(f"{user_num} is positve and even, but less than 50!")
elif user_num >= 0 and user_num > 50 and user_num % 2 != 0:
   print(f"{user_num} is positive, greater than 50 but is odd!")
else:
    print("ERROR: Unknown input")

# =========================================
# =========================================
# ADVANCED CONDITIONAL STATEMENTS TASKS
# =========================================

# Task 11: Complex IF-ELIF-ELSE Chain
# Write a program that asks for the temperature in Celsius and categorizes it as "Cold" (< 10), "Warm" (10-25), or "Hot" (> 25).
# ---
# Hint: Use multiple `elif` statements with different ranges for temperatures.

# Task 12: Nested IF with Multiple Conditions
# Write a program that checks if a student passed or failed. A student passes if the average grade is above 60, and the grades in all subjects are above 50.
# ---
# Hint: Use nested `if` statements and `all()` function for checking multiple grades.

# Task 13: Complex Logical Conditions
# Write a program that checks if a number is a prime number. Use `if`, `else`, and logical operators to implement the check.
# ---
# Hint: Use a loop with `if-else` conditions to check divisibility for prime numbers.

# Task 14: Simulate a Switch Statement Using Dictionary with Functions
# Write a program that asks the user to enter an operation ("add", "subtract", "multiply", "divide") and two numbers. Use a dictionary to map the operation to the correct function and perform the operation.
# ---
# Hint: Use functions for each operation and map them in a dictionary.

# Task 15: Ternary Operators
# Write a program that asks for the user's age and assigns "Adult" if the age is 18 or more, otherwise "Minor". Use a ternary operator.
# ---
# Hint: Use a ternary operation for conditional assignment.

# Task 16: Validating Multiple Conditions
# Write a program that checks if a given password meets the following conditions:
# - Length greater than or equal to 8
# - Contains at least one uppercase letter
# - Contains at least one digit
# ---
# Hint: Use nested `if` statements and string functions like `.isupper()` and `.isdigit()`.

# Task 17: Case-Like Statement with Default Action
# Write a program that asks for a day of the week and prints a message based on the day. Use a dictionary to map days to actions and provide a default action for invalid input.
# ---
# Hint: Use a dictionary with a `.get()` method to handle invalid inputs.

# Task 18: Exception Handling with Conditions
# Write a program that asks for two numbers and an operator (`+`, `-`, `*`, `/`). Perform the operation using an `if-else` structure and handle division by zero with a `try-except` block.
# ---
# Hint: Use `try-except` for handling division by zero, and `if-elif` to handle different operators.

# Task 19: Complex Conditions with Lists and Tuples
# Write a program that asks for a fruit name and checks if it belongs to a list of common fruits (apple, banana, orange). If not, check if it's in a secondary list of rare fruits (dragonfruit, durian).
# ---
# Hint: Use `in` operator with multiple conditions and lists/tuples.

# Task 20: Simulating a Menu System with Nested IF
# Write a program that simulates a basic menu system. It should offer options like "Add", "Delete", "Update", and "View" for a list of items. Use `if-elif-else` to handle different options.
# ---
# Hint: Use nested `if-elif-else` for handling menu options, and loops to keep asking the user until they choose to exit.
