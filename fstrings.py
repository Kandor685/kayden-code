from datetime import datetime
import locale

name = "Mark"
age = 45
print(f"My name is {name} and I am {age} years old")

#############################################################

x = 42
y = 3.14
print (f"x= {x}, y= {y}")

##############################################################

total_cost = 234.1234567
print(f"Total Cost = £{total_cost:.2f}")
###############################################################
population = 7000000000
print(population)
print(f"World Population: {population:,}")

################################################################

now = datetime.now()
print (f"Current Date: {now: %d-%m-%y}")

###############################################################

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
amount = 12345.67
print(f"French Format: {amount:n}")

##############################################################

print(f"{'Name':<10}{'Score':^5}")
print("--------------------------")
print(f"{'Alice':<10}{95:^5}")

###############################################################

value = 0.25
print(f"Percentage: {value: .2%}")

################################################################

data = {"name":"Alice","AGE":30}
print(f"Name: {data['name']}, Age: {data['AGE']}")

items= [1,2,3,4]
print(f"First Item: {items[0]}")

is_logged_in = True
print(f"Status: {'Logged In' if is_logged_in else 'Logged Out'}")
