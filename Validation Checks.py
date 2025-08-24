# def presence_check():
#     while name == "":
#         retry = input("ERROR: No input, Please enter a name: ")
    
def type_check():
    while age != int():
        retry = input("ERROR: Invalid, Please enter an age as an interger: ")
        if age == int():
            break

def range_check():
    if 120 < age or age < 1:
                retry = input("ERROR: Wrong input, Please enter a Valid age: ")
    else:
        print(f"Your name is {name} and you are {age} years old")
        
# name = input("Enter your name: ")
# presence_check()
age = int(input("Enter your age: "))
type_check()
range_check()