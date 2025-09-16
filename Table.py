inValid = True
while inValid:
    number = input("Enter a number between 5 and 10: ")
    try:
        number = int(number)
        if number <= 10 and number >= 5:
            inValid = False
        else:
            print("Number must be between 5 and 10")
    except:
        print("Input must be an integer")
 
for y in range(1,number + 1):
    for x in range(1,number + 1):
        current = x * y
        print(str(current).ljust(4), end="")
    print("")
    print("")