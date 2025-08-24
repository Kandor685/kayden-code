#defining 685 and 327 as an interger and a string

num_int = 685
num_str = "327"

#informing the user what the data type of each set of data is

print("Data type of", num_int, "is", type(num_int))
print("Data type of", num_str, "before Type Casting is", type(num_str))

#casting 327 to be an interger

num_str = int(num_str)
print("Data type of", num_str, "after type casting is", type(num_str))

#add the 2 numbers together

num_sum = num_int + num_str

print("sum of", num_int, "and", num_str, "is", num_sum)
print("Data type of", num_sum, "is", type(num_sum))
