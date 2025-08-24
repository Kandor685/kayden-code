def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by 0"
    finally:
        print("Division complete!")
        
print(divide(3,2))

try:
    
    print(x)
except NameError():
    print("Variable X doesn't exist")
except:
    print("something went wrong!")
    
def divide_numbers(a,b):
    if b == 0:
        print("ERROR: Division by 0 detected. Returning home")
        return None
    else:
        print(a/b)

divide_numbers(a = float(input("Enter a number: ")), b = float(input("What number would you like to divide by? ")))

x = "David"

assert x == "mark", "X should be mark"

import logging
logging.basicConfig(level=logging.info)
logging.info("Program Started")
logging.error("ERROR")