from throw_card_prompt import throw_card_prompt
players_threw = []

def player_turn():

    card_values={
        "Ace": 50,
        "2": 100,
        "3": 150,
        "5": 250,
        "8" : 400,
    }

    
    single_player = ""
    
    while single_player != "King":
        player_threw = []
        single_player = throw_card_prompt()
        if single_player == "King":
            player_threw.append(single_player)
            input("You have voted to skip the challenge. Press Enter to Continue...")
            continue
        elif single_player in card_values:
            player_threw.append(single_player)
            input((f"You threw {player_threw}. Press Enter to Continue..."))
            break
        else: 
            input("Not a valid selection. Press Enter to Continue", end="\r")
            
    players_threw.append(player_threw[0])
    

def players_threw_clear():
    players_threw.clear()




        
 









