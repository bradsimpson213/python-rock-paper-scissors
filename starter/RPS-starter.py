#  ______________________________YOUR CODE BELOW______________________________#

from random import randint

class RPS:
    def __init__(self, players = 1, rounds = 3):
        self.players = players
        self.rounds = rounds
        self.player_wins = 0
        self.computer_wins = 0


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
        while play_count >= n:
            player_choice = input("Pick 'Rock, Paper, or Scissors' ")
            if player_choice != "Rock" or "Paper" or "Scissors":
                print(f'You entered {player_choice}, please enter a valid choice')
                continue
            computer = computer_play()
            round_result = decide_win(player_choice, computer)
        