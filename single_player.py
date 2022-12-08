from os import system
from players import Player, number_of_players
from player_turn import player_turn
# here is where the single player mode will run



def single_player_mode():
    system('clear')
    print ("here we go!")
    for index in range(len(number_of_players())):
        if index == 0:
            print (number_of_players()[0])
            player_turn()
        else:
            return ("buttholes")

single_player_mode()
# print(len(number_of_players()))