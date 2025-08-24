print("Welcome to Python Error Code - project pine tree")
# There are lots of errors with this code (and spellings). 
# Fix the errors so that the code gives the tree as in the 
# example at the end of the code. Values entered between
# 3 and 15 should look recognisable as a pine tree

#subroutine to print a number of characters on the same line
def printChars(NumberOf, chars):
    for I in range (0, NumberOf):
      print(chars, end= "")

#Main program
print("Draw a pine tree")
size = int(input("Enter a size between 3 and 15 "))
posi = 20

#This part draws the main tree using Xs
for i in range(size):
    printChars (posi, " ")
    printChars (i*2+1, "X")
    print()
    posi += -1

#This part draws the trunk using the letter I
for i in range(size // 3):
    printChars(20, " ")
    printChars(1, "I")
    print()


    # *** example correct output ***
    
    # Draw a pine tree
    # Enter a size between 3 and 15 10
    #                 X
    #                XXX
    #               XXXXX
    #              XXXXXXX
    #             XXXXXXXXX
    #            XXXXXXXXXXX
    #           XXXXXXXXXXXXX
    #          XXXXXXXXXXXXXXX
    #         XXXXXXXXXXXXXXXXX
    #        XXXXXXXXXXXXXXXXXXX
    #                 I
    #                 I
    #                 I
