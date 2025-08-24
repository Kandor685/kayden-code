# =========================================
# =========================================
# IF, WHILE, AND FOR LOOPS
# =========================================

# Task 1: Check if a number is positive, negative, or zero
# Write a program that takes an integer as input and prints:
# "Positive" if the number is greater than zero,
# "Negative" if the number is less than zero,
# "Zero" if the number is equal to zero.
# ---

num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} is positive!")
elif num < 0:
    print(f"{num} is negatve!")
else: 
    print(f"{num} is 0")

# Task 2: Find the sum of all even numbers from 1 to 20
# Write a program that calculates and prints the sum of all even numbers
# from 1 to 20 using a while loop.
# ---

evenNumbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Index = 0
Sum = 0
while Index < len(evenNumbers):
    Sum += evenNumbers[Index]
    Index += 1

print (Sum)

# Task 3: Print a multiplication table
# Write a program that takes an integer as input and prints its multiplication
# table from 1 to 10 using a for loop. For example, if the input is 5, the program
# should print:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50
# ---

number = int(input("What Times Table do you want to see? Choose a Number between 1 and 20:  "))

for i in range(10):
    print (number, "x", i+1, "= ", ((i+1) * number))

# Task 4: Calculate the factorial of a number
# Write a program that takes an integer as input and calculates its factorial
# using a while loop. The factorial of a non-negative integer n is the product
# of all positive integers less than or equal to n.
# ---

number = int(input("Enter a Number: "))

factorial = 1

while number > 0:
    factorial *= number
    number -= 1
    
print("Factorial: ", factorial)

# Task 5: Find prime numbers in a given range
# Write a program that takes a range of numbers (start and end) as input and
# prints all prime numbers within that range using a for loop. A prime number
# is a positive integer greater than 1 that has no positive divisors other than 1 and itself.
# ---

Start = int(input("Enter a Number for the start: "))

End = int(input("Enter a Number for the end: "))

for primenum in range (Start, End + 1):
    if primenum > 1:
        is_prime = True
        for primenum in range(2, int(primenum ** 0.5) + 1):
            if primenum % i == 0:
                is_prime = False
        if is_prime:
            print(primenum)

# Task 6: Calculate the sum of digits in a number
# Write a program that takes an integer as input and calculates the sum of its digits
# using a while loop. For example, if the input is 12345, the program should calculate
# and print the sum 1 + 2 + 3 + 4 + 5 = 15.
# ---

number = int(input("Enter a Number: "))

sum_of_digits = 0

while number > 0:
    sum_of_digits += number % 10
    number //= 10

print("Sum of digits:", sum_of_digits)

# Task 7: Determine if a year is a leap year
# Write a program that takes a year as input and determines whether it is a leap year
# or not using an if statement. Leap years are divisible by 4 but not divisible by 100
# unless they are also divisible by 400. If a year is a leap year, print "Leap year";
# otherwise, print "Not a leap year."
# ---

year = int(input("Enter a Year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")


# Task 8: Find the largest number in a list
# Write a program that finds and prints the largest number in a given list of integers
# using a for loop and an if statement. For example, if the list is [5, 12, 9, 23, 7],
# the program should print 23.
# ---



# =========================================
# =========================================
# ADVANCED IF, WHILE, AND FOR LOOPS
# =========================================

# Task 1: Palindrome Checker
# Write a program that takes a string as input and checks if it is a palindrome
# (reads the same forwards and backwards) using an if statement.
# ---


# Task 2: Fibonacci Sequence
# Write a program that generates and prints the first 20 numbers in the Fibonacci sequence
# using a for loop. The Fibonacci sequence starts with 0 and 1, and each subsequent number
# is the sum of the two preceding ones (0, 1, 1, 2, 3, 5, ...).
# ---


# Task 3: Factorization
# Write a program that takes an integer as input and prints its prime factors using
# a while loop. For example, if the input is 12, the program should print "2 2 3" because
# 12 = 2 * 2 * 3.
# ---


# Task 4: Word Frequency Counter
# Write a program that counts the frequency of words in a given text (a long string)
# and prints the word frequencies in descending order using a dictionary and a for loop.
# ---


# Task 5: Pascal's Triangle
# Write a program that generates and prints the first 10 rows of Pascal's Triangle using
# nested for loops. Pascal's Triangle is a triangular array of binomial coefficients.
# ---


# Task 6: Prime Number Generator
# Write a program that generates and prints all prime numbers less than 100 using a for loop
# and a function that checks for prime numbers.
# ---


# Task 7: Number Guessing Game
# Write a number guessing game where the program generates a random number between 1 and 100,
# and the user has to guess the number. Provide hints (higher or lower) and count the number
# of attempts using a while loop.
# ---


# Task 8: File Content Search
# Write a program that reads the content of a text file and allows the user to search for
# a specific word in the file. Display the line numbers where the word is found using a
# for loop.
# ---


# Task 9: Matrix Multiplication
# Write a program that performs matrix multiplication of two given matrices using nested
# for loops. Matrix multiplication is a complex operation involving rows and columns.
# ---


# Task 10: Web Scraper (Advanced)
# Write a program that scrapes data from a website (e.g., a list of articles or products)
# using a Python library like BeautifulSoup or Scrapy. Extract relevant information and
# save it to a file or display it on the console.
# ---

