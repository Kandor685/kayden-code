import random
answer= random.randint(1, 20)
attempts = 1 
guess= int(input("I'm thinking of a number between 1 and 20, can you guess it? "))
while answer != guess and attempts <= 3:
    if answer == guess:
        print("Well Done!")
    else:
        attempts = attempts + 1
        if guess < answer:
            print ("Your Guess Was Too Low!")
            retry = int(input("Try again! "))
        elif guess == answer: 
            print("Your Guess Was Too High!")
            retry = int(input("Try again! "))
        else:
            print("Your Guess Was Too High!")
            retry = int(input("Try again! "))
else:
    print("The Correct Answer Was", answer)
    print("Game Over!")