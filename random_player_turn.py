from throw_card_prompt import random_throw_card_prompt
from throw_card import random_card
random_players_threw = ["Nill"]

def random_player_turn():

    
    card_values={
        "Ace": 50,
        "2": 100,
        "3": 150,
        "5": 250,
        "8" : 400,
        "King": 1000 
    }
    
    single_player = ""
    
    while single_player != "King":
        random_player_threw = []
        single_player = random_card()
        if single_player == "King":
            random_player_threw.append(single_player)
            input("Survivor has voted to skip the challenge. Press Enter to Confirm...")
            continue
        elif single_player in card_values:
            random_player_threw.append(single_player)
            input((f"Survivor threw {random_player_threw}. Press Enter to Confirm..."))
            break
        else:
            print(single_player) 
            input("Not a valid selection. Press Enter to Continue")
    random_players_threw.append(random_player_threw[0])
    print(random_players_threw)

def players_threw_clear():
    random_players_threw.clear()

        
 









