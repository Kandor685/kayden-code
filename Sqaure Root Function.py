def calculate_square_root():

  num = int(input("Enter a number to find the square root: "))

  result = num ** 0.5

  print("The square root of", num, "is", result)



def read_file():

  file = open("data.txt", "r")

  content = file.read()

  print("File Content:\n", content)



def divide_numbers():

  num1 = int(input("Enter the numerator: "))

  num2 = int(input("Enter the denominator: "))

  result = num1 / num2

  print("The result of division is:", result)



# Main program

calculate_square_root()

read_file()

divide_numbers()