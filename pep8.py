import math

#Task 1

#define circle area
def calc_area(radius):
    #calculate the area
    area=math.pi*(radius*radius)
    #print the result
    print(f"Area of the circle: {area}")

#call the function and ask the user for the input
calc_area( radius= float(input("Please enter the radius of the circle: "))) 

#Task 2

#define the function to convert temperature
def temp_convert(User_input):
    #if the user chooses option 1 (convert from celsius)
    if User_input == 1:
        #Ask the user to enter temperature in Celsius
        celsius_convert = float(input("Enter the temperature to be converted (in °C): ")) 
        #Ask user whioch unit they wish to convert to
        Convert_unit = int(input('''Please choose one of the following:
                                 1. Fahrenheit
                                 2. Kelvin
                                ''' ))
        #if the user chooses fahrenheit
        if Convert_unit == 1:
            #convert to fahrenheit
            fahrenheit_converted = (celsius_convert * 9/5) + 32
            #print the result
            print(f"{celsius_convert}°C is: {fahrenheit_converted}°F")
            #ask the user if they wish to use again
            complete = input("Thank you for using the Converter! Would you like to use it again? Y/N: ")
            if complete == "Yes" or complete == "yes" or complete == "y" or complete == "Y" or complete == "YEs" or complete == "yEs" or complete == "yES" or complete == "YeS" or complete == "YES":
             temp_convert(User_input= int(input(''' Welcome to the Temperature Converter! Please Select which unit you wish to convert from:
                                   1. Celsius
                                   2. Fahrenheit
                                   3. Kelvin
                                   ''')))
            elif complete == "No" or complete == "no" or complete == "n" or complete == "N" or complete == "nO" or complete == "NO":
                print("Thank you for using the Temperature Converter, Goodbye!")
                quit()
            else:
                print("ERROR: Unkown Input. Goodbye!")
                quit()
        #if the user chooses Kelvin
        elif Convert_unit == 2:
            #Convert to Kelvin
            Kelvin_converted = (celsius_convert + 273.15)
            #print the result
            print(f"{celsius_convert}°C is: {Kelvin_converted}°K")
            #ask the user if they wish to use again
            complete = input("Thank you for using the Converter! Would you like to use it again? Y/N: ")
            if complete == "Yes" or complete == "yes" or complete == "y" or complete == "Y" or complete == "YEs" or complete == "yEs" or complete == "yES" or complete == "YeS" or complete == "YES":
             temp_convert(User_input= int(input(''' Welcome to the Temperature Converter! Please Select which unit you wish to convert from:
                                   1. Celsius
                                   2. Fahrenheit
                                   3. Kelvin
                                   ''')))
            elif complete == "No" or complete == "no" or complete == "n" or complete == "N" or complete == "nO" or complete == "NO":
                print("Thank you for using the Temperature Converter, Goodbye!")
                quit()
            else:
                print("ERROR: Unkown Input. Goodbye!")
                quit()
        #Anything else
        else:
            #Exit the system
            print("ERROR! Unkown Input! Goodbye!")
            quit()
    #if the user chooses to convert from fahrenheit
    elif User_input == 2:
         #Ask the user to enter temperature in Celsius
        Fahrenheit_convert = float(input("Enter the temperature to be converted (in °F): ")) 
        #Ask user whioch unit they wish to convert to
        Convert_unit = int(input('''Please choose one of the following:
                                 1. Celsius
                                 2. Kelvin
                                ''' ))
        #if the user chooses Celsius
        if Convert_unit == 1:
            #convert to celsius
            Celsius_converted = (Fahrenheit_convert - 32) * 5/9 
            #print the result
            print(f"{Fahrenheit_convert}°F is: {Celsius_converted}°C")
            #Ask whether the user wishes to use the system again
            complete = input("Thank you for using the Converter! Would you like to use it again? Y/N: ")
            if complete == "Yes" or complete == "yes" or complete == "y" or complete == "Y" or complete == "YEs" or complete == "yEs" or complete == "yES" or complete == "YeS" or complete == "YES":
             temp_convert(User_input= int(input(''' Welcome to the Temperature Converter! Please Select which unit you wish to convert from:
                                   1. Celsius
                                   2. Fahrenheit
                                   3. Kelvin
                                   ''')))
            elif complete == "No" or complete == "no" or complete == "n" or complete == "N" or complete == "nO" or complete == "NO":
                print("Thank you for using the Temperature Converter, Goodbye!")
                quit()
            else:
                print("ERROR: Unkown Input. Goodbye!")
                quit()
        #if the user chooses Kelvin
        elif Convert_unit == 2:
            #Convert to Kelvin
            Kelvin_converted = (Fahrenheit_convert  - 32) * 5/9 + 273.15
            #print the result
            print(f"{Fahrenheit_convert}°F is: {Kelvin_converted}°K")
            #Ask whether the user wishes to use the system again
            complete = input("Thank you for using the Converter! Would you like to use it again? Y/N: ")
            if complete == "Yes" or complete == "yes" or complete == "y" or complete == "Y" or complete == "YEs" or complete == "yEs" or complete == "yES" or complete == "YeS" or complete == "YES":
             temp_convert(User_input= int(input(''' Welcome to the Temperature Converter! Please Select which unit you wish to convert from:
                                   1. Celsius
                                   2. Fahrenheit
                                   3. Kelvin
                                   ''')))
            elif complete == "No" or complete == "no" or complete == "n" or complete == "N" or complete == "nO" or complete == "NO":
                print("Thank you for using the Temperature Converter, Goodbye!")
                quit()
            else:
                print("ERROR: Unkown Input. Goodbye!")
                quit()
        #anything else
        else:
            #exit the system
            print("ERROR! Unkown Input! Goodbye!")
            quit()
    if User_input == 3:
        #Ask the user to enter temperature in Kelvin
        Kelvin_convert = float(input("Enter the temperature to be converted (in °K): ")) 
        #Ask user whioch unit they wish to convert to
        Convert_unit = int(input('''Please choose one of the following:
                                 1. Fahrenheit
                                 2. Celsius
                                ''' ))
        #if the user chooses fahrenheit
        if Convert_unit == 1:
            #convert to fahrenheit
            fahrenheit_converted = (Kelvin_convert  - 273.15) * 9/5 + 32
            #print the result
            print(f"{Kelvin_convert}°K is: {fahrenheit_converted}°F")
            #Ask whether the user wishes to use the system again
            complete = input("Thank you for using the Converter! Would you like to use it again? Y/N: ")
            if complete == "Yes" or complete == "yes" or complete == "y" or complete == "Y" or complete == "YEs" or complete == "yEs" or complete == "yES" or complete == "YeS" or complete == "YES":
             temp_convert(User_input= int(input(''' Welcome to the Temperature Converter! Please Select which unit you wish to convert from:
                                   1. Celsius
                                   2. Fahrenheit
                                   3. Kelvin
                                   ''')))
            elif complete == "No" or complete == "no" or complete == "n" or complete == "N" or complete == "nO" or complete == "NO":
                print("Thank you for using the Temperature Converter, Goodbye!")
                quit()
            else:
                print("ERROR: Unkown Input. Goodbye!")
                quit()
        #if the user chooses Celsius
        elif Convert_unit == 2:
            #Convert to Celsius
            celsius_converted = (Kelvin_convert - 273.15)
            #print the result
            print(f"{Kelvin_convert}°K is: {celsius_converted}°C")
            #Ask whether the user wishes to use the system again
            complete = input("Thank you for using the Converter! Would you like to use it again? Y/N: ")
            if complete == "Yes" or complete == "yes" or complete == "y" or complete == "Y" or complete == "YEs" or complete == "yEs" or complete == "yES" or complete == "YeS" or complete == "YES":
             temp_convert(User_input= int(input(''' Welcome to the Temperature Converter! Please Select which unit you wish to convert from:
                                   1. Celsius
                                   2. Fahrenheit
                                   3. Kelvin
                                   ''')))
            elif complete == "No" or complete == "no" or complete == "n" or complete == "N" or complete == "nO" or complete == "NO":
                print("Thank you for using the Temperature Converter, Goodbye!")
                quit()
            else:
                print("ERROR: Unkown Input. Goodbye!")
                quit()
        #Anything else
        else:
            #Exit the system
            print("ERROR! Unkown Input! Goodbye!")
            quit()
    elif User_input == 4:
        print("Thank you for using. Goodbye!")
        quit()
    else:
        print("ERROR! Uknown Input! Goodbye!")
        quit()
        
#call the function
temp_convert(User_input= int(input(''' Welcome to the Temperature Converter! Please Select which unit you wish to convert from:
                                   1. Celsius
                                   2. Fahrenheit
                                   3. Kelvin
                                   4. Exit
                                   ''')))