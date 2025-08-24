def calculator():
    #asking for function
    function = input("Welcome to the Calculator! Would you like to Add (+), Subrtract (-), Multiply (x) or Divide (/)? ")
    #Asking for both numbers for the calculator
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))

    #decide what happens depending on the users input for their function
    if function == "add" or function == "Add" or function == "+":
        print(f"{num1} + {num2} = {num1+num2}")
    elif function == "subtract" or function == "Subtract" or function == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif function == "multiply" or function == "Multiply" or function == "x" or function == "*":
        print(f"{num1} x {num2} = {num1*num2}")
    elif function == "divide" or function == "Divide" or function == "/":
            if num2 == 0:
                print("ERROR: Nothing is divisible by 0!")
            else:    
                print(f"{num1} / {num2} = {num1/num2}")
    else:
        #if the input ins't a mathmatical symbol
        print("ERROR: Unknown input, Try again!")
        calculator()
        
    #ask the user if they wish to use the calculator again 
    complete = input("Thank you for using the calculator! Would you like to use it again? Y/N: ")
    if complete == "Yes" or complete == "yes" or complete == "y" or complete == "Y" or complete == "YEs" or complete == "yEs" or complete == "yES" or complete == "YeS" or complete == "YES":
        calculator()
    elif complete == "No" or complete == "no" or complete == "n" or complete == "N" or complete == "nO" or complete == "NO":
        print("Thank you for using the Calculator, Goodbye!")
        quit()
    else:
        print("ERROR: Unkown Input. Goodbye!")
        quit()
#call the function
calculator()