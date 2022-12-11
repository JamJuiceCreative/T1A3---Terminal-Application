from player_turn import players_threw
from throw_card import random_card
from players import number_of_players




count = 0

def random_player_turn():
    global count
    count+=1
    if count == len(number_of_players()):
        count = 1
    card_values={
        "ace": 50,
        "2": 100,
        "3": 150,
        "5": 250,
        "8" : 400    
    }
    single_player = ""
   
    while single_player != "king":
        

  
        player_threw = []
        single_player = random_card()
        if single_player == "king":
            player_threw.append(single_player)
            input(f"{number_of_players()[count]} has voted to skip the challenge. Press Enter to Confirm...")
            count+=1
            if count == len(number_of_players()):
                count = 1
            continue
        elif single_player in card_values:
            player_threw.append(single_player)
            input((f"{number_of_players()[count]} threw {player_threw[0].capitalize()}. Press Enter to Confirm..."))
                     
            break
        else:
            print(single_player) 
            input("Not a valid selection. Press Enter to Continue")
    players_threw.append(player_threw[0])
    
    
 

def players_threw_clear():
    players_threw.clear()



        
 









