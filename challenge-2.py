##---Challenge 2- creating a simple Rock, Paper Scissor Game

import random

def game_on():
    player1 = input("Please enter '1' for rock, '2' for paper, and '3' for scissors\n")
    comp = random.choice(['R', 'P', 'S'])

    #if user and computer have the same result, ends in tie
    if player1 == comp:
        return "It's a tie"

    #using "if" condition to check who is the winner
    if winner(player1, comp):
        return 'Congrats, You are a Winner'

    return "Sorry, You lost ! Try Again." # this is line execute if the above 2 conditions are not met

#function to determin who win
def winner(player1, player2):
    #using "if" condition to check if player1 wins
    if (player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p') or (player1 == 'p' and player2 == 'r'):
        return True


print(game_on())