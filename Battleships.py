#Complete this simple battleship game
board = [[' ', ' ', '8', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', '8', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', '8', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
boardHits = [[' ', ' ', ' ', ' ',' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

#Initial program announcement
print("Welcome to the Battleship game")
print("Sink the Battleship in 10 goes or less")

#Set initial variables
hits = 0
goes = 0
running = True

while running:
    #Output the board hits with axis using the boardHits array as data (nested for loops needed here)
    print (" 1 2 3 4 5 6 7 8")
    for y in range(8):
        print(y+1, end = '')
        for x in range (8): 
            print(boardHits[y][x], end=" ") 
        print()
        
    #Ask the user for x and y coordinates (subtract 1 for the array index)
    x = int(input("Enter X Coordinates: "))-1
    y = int(input("Enter Y Coordinates: "))-1
    #Add 1 to goes and let the user know how many goes they have had
    goes = goes + 1
    print(f"You've had {goes} goes")
    #Record the go coordinates in the boardHits array (# symbol at the coordinate for hit, - for miss)
    if board [y][x] == '8':
        print ("Hit!")
        boardHits [y][x] = '#'
        hits = hits + 1
    else:
        print("Miss!")
        boardHits [y][x] = '-'
    #Check the board in the coordinate position to see if a hit (#). If so add 1 to hits

    #If ship sunk (hits = 3), annouce game won and the game ends (running = False)
    if hits >= 3 and goes < 13:
        print("Game Over! You Win!")
        running = False
    #else if they are out of goes, annouce game lost and the game ends (running = False)
    elif hits < 3 and goes >= 13:
        print("Game Over! You Lose!")
        print(board)
#Note, you might find it useful to output the board array too until you have everything working

#Once you get the game working, and if time allows consider enhancements to the game.
#Possible enhancements to the game could be:
# If the game lost, show the user where the ship(s) were
# A larger board
# More ships to sink
# Random initial positions of ships (this is advanced)
