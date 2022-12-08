from os import system
from players import Player, number_of_players
from player_turn import player_turn
from list_of_challenges import number_of_challenges
# here is where the single player mode will run

list_of_inputs = []
survivor1 = []
survivor2 = []
survivor3 = []

def single_player_mode():
    system('clear')
    print ("here we go!")
    for index in range(len(number_of_players())):
        if index == 0:
            print (number_of_players()[0])
            print (number_of_challenges()[0])
            player_turn()
        else:
            return ("buttholes")

single_player_mode()
# print(len(number_of_players()))
