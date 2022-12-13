from os import system
from throw_card_prompt import throw_card_prompt
from card_values import card_values

players_threw = []

def player_turn():
    

    single_player = ""
    
    while single_player != "king":
        player_threw = []
        single_player = throw_card_prompt()
        if single_player == "king":
            player_threw.append(single_player)
            input("You have voted to skip the challenge. Press Enter to Continue...")
            continue
        elif single_player in card_values:
            player_threw.append(single_player)
            input((f"You threw {player_threw[0].capitalize()}. Press Enter to Continue..."))
            break
        else: 
            input("Not a valid selection. Press Enter to Continue...")
            
    players_threw.append(player_threw[0])
    
    

def players_threw_clear():
    players_threw.clear()






