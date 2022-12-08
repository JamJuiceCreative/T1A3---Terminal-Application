from os import system
from throw_card_prompt import throw_card_prompt


def player_turn():

    
    card_values={
        "Ace": 50,
        "2": 100,
        "3": 150,
        "5": 250,
        "8" : 400, 
    }
    
    single_player = ""
    player_threw = []
    while single_player != "King":
        
        single_player = throw_card_prompt()
        if single_player in card_values:
            player_threw.append(single_player)
            print(f"You threw {player_threw}")
            
        elif single_player == "King":
            break
        else: 
            print("That's not a valid option!")
        
        system('clear')
    input("press Enter to continue...")



        
   








