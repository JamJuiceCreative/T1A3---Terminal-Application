from os import system
from players import Player, number_of_players
from player_turn import player_turn, players_threw, players_through_clear
from list_of_challenges import number_of_challenges
from instructions import instructions

# here is where the single player mode will run

# list_of_inputs = []
# list_of_inputs.append(player_threw)
# survivor1 = [list_of_inputs[0]]
# survivor2 = [list_of_inputs[1]]
# survivor3 = [list_of_inputs[2]]

# def do_cards_match():
#     while survivor1 != survivor2 and survivor3:
#         print ("this is a test")
# print ("those bad boys match")

# do_cards_match()



sum_of_inputs = []
count = 0
def single_player_mode():
    global count
    count +1
    system('clear')
    instructions()
    list_of_inputs = []
    

    for index in range(len(number_of_players())+1):
        
        
        if index == 0:
            print (number_of_players()[0])
            print(f"Round:{count+1}")
            print (number_of_challenges()[0])
            player_turn()
            list_of_inputs.append(players_threw[0])
            input((list_of_inputs[0]))
        elif index == 1:
            system('clear')
            instructions()
            print()
            print (number_of_players()[1])
            print(f"Round:{count+1}")
            print (number_of_challenges()[0])
            player_turn()
            list_of_inputs.append(players_threw[1])
            input((list_of_inputs[1]))
        elif index == 2:

            system('clear')
            instructions()
            print()
            print (number_of_players()[2])
            print(f"Round:{count+1}")
            print (number_of_challenges()[0])
            player_turn()
            list_of_inputs.append(players_threw[2])
            input((list_of_inputs[2]))
        elif index >= 3:
            # check if all items in list_of_inputs are the same
            if([list_of_inputs[0]]*len(list_of_inputs) != list_of_inputs):
        
                sum_of_inputs.append(list_of_inputs)
                input(sum_of_inputs)
                # list_of_inputs.clear()
                input(list_of_inputs)
                players_through_clear()
                single_player_mode()
            elif([list_of_inputs[0]]*len(list_of_inputs) == list_of_inputs):
                sum_of_inputs.append(list_of_inputs)
                players_through_clear()
                count +=1
                single_player_mode()
        else:
            single_player_mode()
       

single_player_mode()

