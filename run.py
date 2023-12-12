import random


# Get inputs like row and column,Input to exit the game

def get_shot(guesses):
    while True:
        row = input("Please enter the row (0 - 6): ")
        if row.lower() == "exit":
            return "exit"
          
        try:
            row = int(row)
            col = int(input("Please enter the column (0 - 6): "))

            shot = 7 * row + col

            if shot < 0 or shot > 48:
                print("Incorrect coordinates, Please try again")
            elif shot in guesses:
                print("Incorrect, it's been used already")
            else:
                return shot
        except ValueError:
            print("Incorrect entry,Please enter your number.")


# Creating the board

def show_board(hit, miss):
    print("===== BATTLESHIP Board =====")
    print("    0  1  2  3  4  5  6 ")
    place = 0
    for x in range(7):
        row = ""
        for y in range(7):
            if place in hit:
                ch = " X "
            elif place in miss:
                ch = " O "
            else:
                ch = " * "
            row += ch
            place += 1
        print(x, "", row)


# Check if its a miss or hit

def check_shot(shot, boat, hit, miss):
    if shot in boat:
        boat.remove(shot)
        hit.append(shot)
    else:
        miss.append(shot)
    return boat, hit, miss


# Random places in the board

def generate_random_boats():
    boats = []
    while len(boats) < 3:
        new_boat = random.randint(0, 48)
        if new_boat not in boats:
            boats.append(new_boat)
    return boats


# Fuction after player types "exit"

def exit_game():
    user_input = input("Do you want to exit the game? (yes / no): ")
    return user_input.lower() == "yes"


# Commands to hit ,miss and checks ships found

def play_battleship_game():
    hit = []
    miss = []
    ships_found = 0

    player_name = input("Enter your name: ")
    print("\n")
    print(f"READY {player_name}! Let's play Battleship.")
    print("\n")

    # Generate 3 random hidden boat positions

    boat = generate_random_boats()
    hidden_boats = ['?' for _ in range(48)]

    # Instructions how to play the game

    print("You have a total of 20 turns to sink 3 hidden ships.")
    print("Guess a row and a column (0 - 6).")
    print(" You will see X when you hit a ship,Otherwise O if you miss.")
    print("Type'exit' instead of row number if you want to quit")
    print("Choose Wisely,GOODLUCK!")
    print("\n")

    turns_remaining = 20

    # Starting the game loop

    for i in range(turns_remaining):
        print(f"Turns left: {turns_remaining - i}")
        show_board(hit, miss)
        guesses = hit + miss
        shot = get_shot(guesses)
        print("\n")

        # Player to exit the game

        if shot == "exit":
            if exit_game():
                return

        try:
            shot = int(shot)
            if shot < 0 or shot > 48:
                print("Incorrect number, please try again.")
            elif shot in guesses:
                print("Incorrect number, it's been used before.")
            else:
                boat, hit, miss = check_shot(shot, boat, hit, miss)
                if shot in boat:
                    ships_found += 1
                    print(f"You've hit one! Total found: {ships_found}")
                    if ships_found == 3:
                        print("Congrats!You have sunk 3 ships.You WIN!")
                        if exit_game():
                            return
        except ValueError:
            print("Incorrect entry - please enter your guess as a number.")
            print("\n")

        # Check if the game is over by winning or losing

        if len(boat) == 0:
            print("Congratulations! You've sunk all the battleships.You WIN!")
            if exit_game():
                return

    if len(boat) > 0:
        print(" ===== GAMEOVER!Better luck next time! ===== ")


# Start the game

play_battleship_game()
