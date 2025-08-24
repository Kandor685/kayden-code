class car:
    def __init__(self, make, model, colour, price):
        self.make = make
        self.model = model
        self.colour = colour
        self.price = price

    def printDetails(self):
        print(f"The {self.make} is a {self.colour} {self.model} and costs ${self.price}.")

class Employee:
    def __init__(self, base_salary, overtime_hours, overtime_rate):
        self.base_salary = base_salary
        self.overtime_hours = overtime_hours
        self.overtime_rate = overtime_rate

    def getWage(self):
        if self.overtime_hours < 0 or self.overtime_rate < 0:
            raise ValueError("Overtime hours and rate must be non-negative.")
        return self.base_salary + (self.overtime_hours * self.overtime_rate)

    def calculateTimeToAffordcar(self, car_price):
        wage = self.getWage()
        time_in_years = car_price / wage
        return time_in_years

mustang = car("Ford", "Mustang 5.0 V8 GT Shadow Edition", "Shadow Black", 55000)
citroen = car("Citroen", "C1 1.0 VTi Feel 5dr", "Red", 12000)

employee1 = Employee(30000, 10, 20)

time_to_afford_mustang = employee1.calculateTimeToAffordcar(mustang.price)
time_to_afford_citroen = employee1.calculateTimeToAffordcar(citroen.price)

mustang.printDetails()
print(f"It will take approximately {time_to_afford_mustang:.2f} years to afford the Mustang.")

citroen.printDetails()
print(f"It will take approximately {time_to_afford_citroen:.2f} years to afford the Citroen.")