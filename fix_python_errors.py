#Each exercise is seperated out by muli line comments which you can delete/insert as needed





#### EX1 Code:
def calculate_area(width, height):
    area = width * height
    return area

# Example usage
print(calculate_area(5, 10))



#### EX2 Code:
def multiply_list(numbers, multiplier):
    result = []
    for num in numbers:
        result.append(num * multiplier)
    return result

# Example usage
print(multiply_list([1, 2, 3, 4], 2))



#### EX3 Code:
def get_element(lst, index):
    return lst[index]

# Example usage
print(get_element([10, 20, 30, 40], 2))



#### EX4 Code:
def greet_user(name, age):
    return ("Hello ", name, ", you are ", age, "years old.")

# Example usage
print(greet_user("Alice", 30))


'''
#### EX5 Code:
def is_even(num):
    if num % 2 = 0:
        return True
    else:
        return False

# Example usage
print(is_even(4))
'''


#### EX6 Code:
def remove_odd_numbers(numbers):
    for num in numbers:
        if num % 2 != 0:
            numbers.remove(num)
    return numbers

# Example usage
print(remove_odd_numbers([1, 2, 3, 4, 5, 6]))




#### EX7 Code:
def get_student_grade(students, name):
    return students.get(name, "Student not found")

# Example usage
students = {"Alice": "A", "Bob": "B", "Charlie": "C"}
print(get_student_grade(students, "David")) 



'''
#### EX8 Code:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1

# Example usage
print(factorial(5))
'''


#### EX9 Code:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display_info():
        print(f"Name: {self.name}, Age: {self.age}")

# Example usage
Person = Person("Alice", 30)
Person.display_info()


'''
#### EX10 Code:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, salary):
        super.__init__(name, age)
        self.salary = salary
        
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

# Example usage
employee = Employee("Bob", 40, 50000)
employee.display_info()
'''