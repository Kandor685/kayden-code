#task 1

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
num3 = float(input("Enter 3rd number: "))

total = num1 + num2 + num3

mean = total / 3

print (f"The average of {num1}, {num2} and {num3} is {mean}")

#task 2

# incorrect version:
# area = length * width
# length = float(input("Enter the Length: "))
# width  = float(input("Enter the Width: "))

# corrected version:

width  = float(input("Enter the Width: "))
length = float(input("Enter the Length: "))
area = length * width
print(f"The area of the rectangle is {area}")

