def Calculator():
    symbol=input("Welcome to the calculator! Would you like to Add, Subtract, Multiply or Divide? ")
    if symbol == "Add" or symbol == "add":
        num1 = int(input("Input First Number: "))
        num2 = int(input("Input Second Number: "))
        print (num1, "+", num2, "=", num1 + num2)
    elif symbol == "subtract" or symbol == "Subtract":
        num1 = int(input("Input First Number: "))
        num2 = int(input("Input Second Number: "))
        print (num1, "-", num2, "=", num1 - num2)
    elif symbol == "Multiply" or symbol == "multiply":
        num1 = int(input("Input First Number: "))
        num2 = int(input("Input Second Number: "))
        print (num1, "x", num2, "=", num1 * num2)
    elif symbol == "Divide" or symbol == "divide":
        num1 = int(input("Input First number: "))
        num2 = int(input("Input Second Number: "))
        print (num1, "/", num2, "=", num1 / num2)
    else:
        print ("Error! Unkown Input")
        Calculator()
    retry= input("Would you like to use the calculator again? Y/N: ")
    if retry == "Y" or retry == "y":
        Calculator()
    elif retry == "N" or retry == "n":
        print ("Thank you for using the Calculator, goodbye!")
        quit()
    else:
        print ("Error! Unkown Input! Goodbye!")
        quit()
Calculator()