def get_user_input():
    while True:
        try:
            user_input = input("Enter a number between 1 and 100: ")
            number = float(user_input)
            if 1 <= number <= 100: 
                return number
            else:
                print("ERROR: Number is out of range. Enter a number between 1 and 100: ")
        except ValueError:
            print("ERROR: Invalid input, Enter a number within the range of 1-100:")

number = get_user_input()
print(f"Number within range! You entered: {number}")
