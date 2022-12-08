from os import system
from throw_card_prompt import throw_card_prompt

player_threw = []
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
        
        single_player = throw_card_prompt()
        if single_player == "King":
            player_threw.append(single_player)
            print("You have decided to skip the challenge")
            break    
        if single_player in card_values:
            player_threw.append(single_player)
        print(f"You threw {player_threw}")
        break
    
 
        
    #     elif single_player == "King":
    #         continue
    #     else: 
    #         print("That's not a valid option!")
        
    #     system('clear')
    # print ("WTF mate")





        
 









