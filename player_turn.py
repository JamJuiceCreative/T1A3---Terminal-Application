
from throw_card_prompt import throw_card_prompt

players_threw = []
def player_turn():

    
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
        player_threw = []
        single_player = throw_card_prompt()
        if single_player == "King":
            player_threw.append(single_player)
            print("You have decided to skip the challenge")
            break    
        if single_player in card_values:
            player_threw.append(single_player)
        input((f"You threw {player_threw}. Press Enter to Continue..."))
        break
    
# player_turn()
        
    #     elif single_player == "King":
    #         continue
    #     else: 
    #         print("That's not a valid option!")
        
    #     system('clear')
    # print ("WTF mate")





        
 









