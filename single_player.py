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
    print ("Throw a card either Ace, 2, 3, 5, 8 or King, Ace being task is easy to 8 being task is hard. Throw a king and automatically skip the challenge.")
    for index in range(len(number_of_players())):
        if index == 0:
            print (number_of_players()[0])
            print (number_of_challenges()[0])
            player_turn()
                # if player_turn == "King"
                #     index += index 
        else:
            return ("buttholes")

single_player_mode()
# print(len(number_of_players()))
