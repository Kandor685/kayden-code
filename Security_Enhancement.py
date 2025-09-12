filename = "passwordfile.txt"
file = open(filename, "r")
password = file.read().strip()
file.close()

entered_password = ""

while entered_password != password:
    entered_password = input("Enter the password: ")
    if entered_password == password:
        print("Access granted")
    else:
        print("Access denied")

print("Welcome to our security system")
