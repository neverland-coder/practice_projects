import random


def gameplay():
    games_played = 0
    rounds_won = 0
    valid_selection = ['rock', 'paper', 'scissors']
    while games_played < 5 or rounds_won == 3:
        user = input("Select one of the following options: rock, paper, scissors: ").lower()
        computer = random.choice(['rock', 'paper', 'scissors'])
        if user not in valid_selection:
            print("That is not a valid selection")
        elif user == computer:
            print(f"You've selected {user}")
            print("The match is a draw.")
            games_played += 1

        elif (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
            rounds_won += 1
            print(f"You've selected {user}, the computer has selected {computer}")
            print(f"You've won {rounds_won} round/s!")
            games_played += 1
        else:
            print(f"You've selected {user}, the computer has selected {computer}")
            print("You've lost the round!")
            games_played +=1


gameplay()



