import random


def get_shot(guesses):
    while True:
        try:
            shot =input("Please enter your guess: ")
            if shot.lower() == "exit":
                return "exit"
            shot = int(shot)
            if shot < 0 or shot > 49:
                print("Incorrect number,Please try again")
            elif shot in guesses:
                print("Incorrect number,it's been used already")
            else:
                ok = "y"
                break
        except ValueError:
            print("Incorrect entry,Please enter your number.")
    return shot


def show_board(hit, miss):
    print("---- Player Board ----")
    print(" 0 1 2 3 4 5 6 ")
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
            print(x, " ", row)


def check_shot(shot, boat1, hit, miss, comp):
    if shot in boat1:
        boat1.remove(shot)
        if len(boat1) > 0:
            hit.append(shot)
    else:
        miss.append(shot)
    return boat1, hit, miss, comp


def generate_random_boats():
    boats = []
    while len(boats) < 5:
        new_boat = random.randint(0, 99)
        if new_boat not in boats:
            boats.append(new_boat)
    return boats


def play_battleship_game():
    hit = []
    miss = []
    comp = []

    player_name = input("Enter your name: ")
    print(f"Ready {player_name}! Let's play Battleship.")

   