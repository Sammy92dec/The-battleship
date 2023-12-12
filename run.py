import random


def get_shot(guesses):
    while True:
        row = input("Please enter the row (0-6): ")
        if row.lower() == "exit":
            return "exit"

        try:
            row = int(row)  
            col = int(input("Please enter the column (0-6): "))

            shot = 7 * row + col

            if shot < 0 or shot > 48:
                print("Incorrect coordinates, Please try again")
            elif shot in guesses:
                print("Incorrect, it's been used already")
            else:
                return shot
        except ValueError:
            print("Incorrect entry,Please enter your number.")


def show_board(hit, miss):
    print("---- Player Board ----")
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


def check_shot(shot, boat, hit, miss):
    if shot in boat:
        boat.remove(shot)
        hit.append(shot)
    else:
        miss.append(shot)
    return boat, hit, miss


def generate_random_boats():
    boats = []
    while len(boats) < 5:
        new_boat = random.randint(0, 48)
        if new_boat not in boats:
            boats.append(new_boat)
    return boats


def exit_game():
    user_input = input("Do you want to exit the game? (y/n): ")
    return user_input.lower() == "y"


def play_battleship_game():
    hit = []
    miss = []

    player_name = input("Enter your name: ")
    print(f"Ready {player_name}! Let's play Battleship.")
      
    # Generate 5 random hidden boat positions 
    boat = generate_random_boats()
    hidden_boats = ['?' for _ in range(48)]

    # Instructions how to play the game
    print("You have a total of 10 turns to try sinking the compnent's ships.")
    print("Guess a number from 0-48.You will see X when you hit a ship")
    print("Otherwise O if you miss.")
    print("Choose Wisely ,GOODLUCK!")

    turns_remaining = 20
    revealed_boats = []
    for i in range(turns_remaining):
        print(f"Turns left: {turns_remaining - i}")
        show_board(hit, miss)
        guesses = hit + miss
        shot = get_shot(guesses)

        # Player to exit the game
        if shot == "exit":
            if exit_game():
                return

        if shot == "help":
            hint_indices = [i for i, x in enumerate(hidden_boats) if x == '?']
            if hint_indices:
                hint_index = random.choice(hint_indices)
                print(f"HINT: One of the boats is at {boat[hint_index]}.")
                hidden_boats[hint_index] = str(boat[hint_index])
                show_board(hit, miss)
            else:
                print("No more hidden boats for hint.")
            continue  

        try:
            shot = int(shot)
            if shot < 0 or shot > 48:
                print("Incorrect number, please try again.")
            elif shot in guesses:
                print("Incorrect number, it's been used before.")
            else:
                boat, hit, miss = check_shot(shot, boat, hit, miss)
        except ValueError:
            print("Incorrect entry - please enter your guess as a number.")
        
        # Check if the game is over by winning or losing
        if len(boat) == 0:
            print("Congratulations! You've sunk all the battleships. You win!")
            if exit_game():
                return
         
    if len(boat) > 0:
        print("Game Over!Better luck next time!")


play_battleship_game()