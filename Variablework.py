#define the global variable
counter = 10

# #define the function
def increment_counter():
    counter = 5
    print(counter)
increment_counter()
print(counter)

#define the global variable
counter = 10
print(counter)
#define function

def modify_counter():
    global counter 
    counter = counter + 1
    print("This is a global variable {counter}")
modify_counter()