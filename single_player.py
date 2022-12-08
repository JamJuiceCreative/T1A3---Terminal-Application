from os import system
from players import Player, number_of_players
from player_turn import player_turn, player_threw
from list_of_challenges import number_of_challenges
# here is where the single player mode will run

list_of_inputs = [2, 2, 2]
survivor1 = [list_of_inputs[0]]
survivor2 = [list_of_inputs[1]]
survivor3 = [list_of_inputs[2]]

def do_cards_match():
    while survivor1 != survivor2 and survivor3:
        print ("this is a test")
print ("those bad boys match")

do_cards_match()

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
            index += index
        if index == 1:
            print ("yay, it worked")
        elif index == 2:
            print ("yay it worked again")
        elif index == 3:
            print ("This shouldn't work")
        else:
            print(list_of_inputs)
            

    

# single_player_mode()
# print(len(number_of_players()))
# single_player_mode()
