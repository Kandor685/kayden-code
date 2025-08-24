#define the function
def calculate_average(numbers):
    #Ensure list isn't empty
    try:
        if len(numbers) == 0:
            return ("List cannot be empty!")
        #define total 
        total = sum(numbers)
        count = len(numbers)
        
        average = total/count
        return average
    
    except ValueError:
        print("All inputs must be numbers.")

numbers = []
numenter = float(input("Enter a number or type 'calculate' to stop: "))


while numenter == float or numenter != 'Calculate' or numenter != 'calculate':
    numbers.append(numenter)
    numenter = (input("Enter a another number or type 'calculate' to stop: "))
    if numenter == 'calculate' or numenter == 'Calculate':
        break
try:
    numbers_float = list(map(float, numbers))
    print("Average: ", calculate_average(numbers_float))
except ValueError:
    print("ERROR: Must be numbers")
