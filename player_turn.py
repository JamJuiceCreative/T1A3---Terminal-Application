from os import system
from list_of_challenges import challenge1, challenge2, challenge3
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
    survivor1 = []
    while single_player != "King":
        single_player = throw_card_prompt()
        if single_player in card_values:
            survivor1.append(single_player)  
            print(survivor1)
        elif single_player == "King":
            continue
        else: 
            print("That's not a valid option!")
        input("press Enter to continue...")
        system('clear')
    print("You have chosen to skip the challenge")



        
   








