#Task 1
# retireage = 65
# userage = int(input("Enter Your Age: "))
# if userage >= retireage:
#     print("You're already retired!")
# elif userage < 0: 
#     print("You're not even born!")
# else:
#     print("You have", retireage - userage, "years until you retire!")

#Task 2
# import random
# def number_guessing_game():
#     number_to_guess = random.randint(1, 100)
#     print("Welcome to the Number Guessing Game!")
#     print("I have selected a number between 1 and 100.")
#     guessed_correctly = False
    
#     guesscount = 0
    
#     while guesscount < 5 and not guessed_correctly: 
#         try:
#             guess = int(input("Enter your guess: "))
            
#             if guess < number_to_guess:
#                 print("Too low!")
#                 guesscount += 1
#             elif guess > number_to_guess:
#                 print(f"Too high!")
#                 guesscount += 1
#             else:
#                 print("Congratulations! You guessed the correct number.")
#                 guessed_correctly = True
#         except ValueError:
#             print("Please enter a valid number.")
#     if not guessed_correctly:
#         print(f"Game Over! The correct number was {number_to_guess}.")
# number_guessing_game()

#task 3

prices = [20, 150, 50]
Quantities = [2, 1, 3]
