#  we wil make a programm for playing 
# rock paper scissors game with the computer.
import random

def play ():

    print("Welcome to Rock Paper Scissors Game!")
    print()
    user = input(f"whats your choice ? 'r' for rock, 'p' for paper and 's' for scissors \n")

# we let the computer choice also
    computer = random.choice(['r', 'p' , 's'])

    if user == computer:
        return " It's tie"
    
    if is_win(user, computer):
        return f"You won this round {user} beats {computer}"
    
    return "you lost!"

def is_win (player , opponent):
    # return true if player wins
    #  r > s , s > p , p > r 
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
    # elif (player == 's' and opponent == 'p') or (player == 'p' and opponent == 's'):
    #     return True
print(play())


