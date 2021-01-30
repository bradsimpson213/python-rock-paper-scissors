# PROBLEM 11 - BONUS: Rock, Paper, Scissors! 🪨 📃 ✂️
#
# Implement playing Rock, Paper, Scissors against the computer!  Here are the
# specifications:
# 
#  1. Define a function named "play_rock_paper_scissors" that takes in one
#     arguement, which should be an integar value for the number of rounds to
#     play.
#  2. Check to make sure the integar value passed in as the arguement to
#     "play_rock_paper_scissors" is an odd number (so there will have to be a
#     winner decided).
#  3. Get user/player input and save it to a variable.  Input must be in the
#     format of "Rock", "Paper", or "Scissors".
#  4. Generate a random play from the computer (picking one from a list or other
#     appropraite data structure containing "Rock, Paper, Scissors" to put up
#     against the user/player input).
#
#  Hints:  Maybe make a helper function to generate the computers choice
#  and/or to determine who wins each round.
#
#  ______________________________YOUR CODE BELOW______________________________#

from random import randint

def computer_play():
    choices = ("Rock", "Paper", "Scissors")
    choice_num = randint(0, 2)
    return choices[choice_num]

def decide_win(s1, s2):
    if s1 == "Rock" and s2 == "Rock":
        return None
    if s1 == "Paper" and s2 == "Paper":
        return None
    if s1 == "Scissors" and s2 == "Scissors":
        return None
      

def play_rock_paper_scissors(n):
    play_count = 0
    player_wins = 0
    computer_wins = 0
    while play_count >= n:
        player_choice = input("Pick 'Rock, Paper, or Scissors' ")
        if player_choice != "Rock" or "Paper" or "Scissors":
            print(f'You entered {player_choice}, please enter a valid choice')
            continue
        computer = computer_play()
        round_result = decide_win(player_choice, computer)
        