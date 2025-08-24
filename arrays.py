cars = []
car = ""

while car != "Exit":
    car = input("Enter a car brand, or say Exit to stop and print the list: ")
    if car != "Exit":
        cars.append(car)


print(cars)