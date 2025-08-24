import random

# Snakes and Ladders positions
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def roll_dice():
    return random.randint(1, 6)

def move_player(position):
    if position in snakes:
        print(f"Oh no! Landed on a snake! Moving down from {position} to {snakes[position]}")
        return snakes[position]
    elif position in ladders:
        print(f"Yay! Climbed a ladder! Moving up from {position} to {ladders[position]}")
        return ladders[position]
    return position

def play_game():
    players = [0, 0]  # Player positions
    current_player = 0

    while True:
        input(f"Player {current_player + 1}, press Enter to roll the dice...")
        dice = roll_dice()
        print(f"Player {current_player + 1} rolled a {dice}")
       
        new_position = players[current_player] + dice
        if new_position > 100:
            print(f"Player {current_player + 1} cannot move. Position remains {players[current_player]}")
        else:
            players[current_player] = move_player(new_position)
            print(f"Player {current_player + 1} is now on square {players[current_player]}")
       
        if players[current_player] == 100:
            print(f"Player {current_player + 1} wins!")
            break
       
        current_player = 1 - current_player  # Switch players

if __name__ == "__main__":
    play_game()
