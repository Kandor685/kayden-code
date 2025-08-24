import math

def area_and_perimeter_calc():
    shape = input("Calculate for Triangle or Rectangle? ")
        
    if shape == "Rectangle" or shape == "Rectangle":
        #ask the user for base and height
        base = float(input("Enter the base of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))

        #calculate area
        area = (base * height)

        # output area
        print(f"Area of rectangle: {area}")

        #Define a, b and c for pythag
        a = base
        b = height

        #calculate the diagonal line

        c = (a*a) + (b*b)
        
        #calculate perimeter
        perimeter = (base * 2) + (height * 2)

        #print perimeter
        print(f"Perimeter is: {perimeter}")

        print(f"The Diagonal length of the rectangle is: ", math.sqrt(c))
    elif shape == "Triangle" or shape == "triangle":
        #ask the user for base and height
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))

        #calculate area
        area = ((base * height)/2)

        # output area
        print(f"Area of rectangle: {area}")

        #Define a, b and c for pythag
        a = base
        b = height

        #calculate the diagonal line

        c = (a*a) + (b*b)
        print(f"The Diagonal length of the Triangle is: ", math.sqrt(c))    
        
        #define perimeter
        
        perimeter = a + b + c
        
        #print perimeter
        
        print(f"Perimeter is: {perimeter}")

    else:
        print("ERROR: Unknown input. Goodbye!")
        area_and_perimeter_calc()
    repeat = input("Would you like to use again? ")
    
    if repeat == "Yes" or repeat == "yEs" or repeat == "yeS" or repeat == "YEs" or repeat == "YeS" or repeat == "yES" or repeat == "YES" or repeat == "yes" or repeat == "y" or repeat == "Y":
        area_and_perimeter_calc()
    elif repeat == "No" or repeat == "nO" or repeat == "No" or repeat == "NO" or repeat == "no" or repeat == "N" or repeat == "n":
        print("Thank you for using! Goodbye!")
        exit()
    else:
        print("ERROR: Unkown Input. Goodbye!")
        exit()
area_and_perimeter_calc()