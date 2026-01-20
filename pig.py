import random


player_score = 0
computer_score = 0
turn_total = 0

def roll_die():
    return random.randint(1,6)

def player_turn(player_score, turn_total):
    print(f"Total Score: {player_score}")
    move = input("Do you want to Roll or Hold (R or H)")
    if move == "R":
        roll = roll_die()
        if roll != 1:
            print(f"You rolled a {roll}")
            turn_total += roll
            print(f"Turn Total: {turn_total}")
            player_score += roll
            player_turn(player_score, turn_total)
        else:
            print("You rolled a 1")
            player_score -= turn_total
            turn_total = 0
            print(f"Total Score: {player_score}")
    elif move == "H":
        player_score += turn_total
        turn_total = 0
    else:
        print("Invalid Input: Please Try Again")
        player_turn(player_score, turn_total)

def computer_turn(computer_score, turn_total):
    print(f"Computer Score: {computer_score}")

first_turn = random.randint(0,1)

if first_turn == 0:
    player_turn(player_score, turn_total)
else:
    computer_turn(computer_score, turn_total)