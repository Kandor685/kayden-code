number = float(input("Enter a number between 1 and 10: "))


flag = True
while float(number) < 1 or number > 10:
    print("Invalid number, try again.")
    number = float(input("Enter a number between 1 and 10: "))
    flag = True
else:
    print(number)
    flag = False 