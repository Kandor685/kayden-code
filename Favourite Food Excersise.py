# This program will ask the user to enter their favourite food, then assign it to a variable and display it

# ----------------
# Subprograms
# ----------------
def favourite_food():# <----------- Defining a Subprogram
  food = "Chocolate" # <----- String
  print(food)

# ----------------
# Main program
# ----------------
favourite_food() # <------- Calling a Subprogram

def favourite_animal():
    animal = input("Enter Your Favourite Animal: ")
    print(f"Your Favourite Animal is {animal}!")
favourite_animal()