# Project Fibonnaci Sequence

def generate_next_term(first_term, second_term):
  next_term = first_term + second_term
  return next_term

print("Welcome to the Fibonacci Sequence generator!")
number_of_terms = int(input("How many terms would you like? "))

first_term = 0
second_term = 1

number_of_terms_generated = 0
while number_of_terms_generated < number_of_terms:
  print(first_term) 
  next_term = generate_next_term(first_term, second_term)
  first_term = second_term
  second_term = next_term
  number_of_terms_generated += 1

#Project Password Checker
PASSWORD = "LetMeIn"


User_name = input("Welcome! Please Enter Your Username (Case Sensitive!): ")

while User_name != "User": 
    User_name = input("ERROR: Unkown User! Try Again: ")

password = input("Welcome User! Enter Your Password: ")


while password != PASSWORD:
    password = input("INCORRECT! Try again: ")

else:
    print("Welcome User! Successfully Logged In!")