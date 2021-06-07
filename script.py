# Importing the modules
from random import choice, randint
import time
# The choices
options = ["rock", "paper", "scissors"]
# Number of times the user wants to play
rounds = int(input("Enter the number of rounds you want to play : "))
# Number of rounds played
rounds_played = 0
# No of wins
player_wins = 0
computer_wins = 0


def checkWinner(player, computer):
    if player == "rock" and computer == "scissors":
        return "player"
    elif player == "scissors" and computer == "paper":
        return "player"
    elif player == "paper" and computer == "rock":
        return "player"
    elif computer == "rock" and player == "scissors":
        return "computer"
    elif computer == "scissors" and player == "paper":
        return "computer"
    elif computer == "paper" and player == "rock":
        return "computer"
    else:
        return "tie"


# The loop
while rounds_played < rounds:
    player_choice = input("Choose from rock, paper and scissors : ").lower()
    print("\n")
    computer_choice_index = randint(0, 2)
    computer_choice = options[computer_choice_index]
    winner = checkWinner(player_choice, computer_choice)
    if winner == "player":
        time.sleep(2)
        print(f"Computer chose {computer_choice}")
        print("You win this round !!!")
        print("\n")
        player_wins += 1
    elif winner == "computer":
        time.sleep(2)
        print(f"Computer chose {computer_choice}")
        print("Computer wins this round.")
        print("\n")
        computer_wins += 1
    else:
        time.sleep(2)
        print(f"Computer chose {computer_choice}")
        print("Nobody won this round. Its a tie !")
        print("\n")
    rounds_played += 1

# Anouncing the total winner
if player_wins > computer_wins:
    time.sleep(2)
    print(
        f"You won {player_wins} round(s) and the computer won {computer_wins} round(s).")
    print("You won this match !!!")
elif computer_wins > player_wins:
    time.sleep(2)
    print(
        f"You won {player_wins} round(s) and the computer won {computer_wins} round(s).")
    print("Computer wins this match. Better luck next time.")
else:
    time.sleep(2)
    print(
        f"You won {player_wins} round(s) and the computer won {computer_wins} round(s).")
    print("This match is a draw.")
