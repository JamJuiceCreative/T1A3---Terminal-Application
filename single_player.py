from os import system
from list_of_challenges import challenge1, challenge2, challenge3
from throw_card_prompt import throw_card_prompt

card_values={
    "Ace": 50,
    2: 100,
    3: 250,
    5: 500,
    8: 750,
    "King": 1000
}
print('Ace' in card_values.values())

single_player = ""
survivor1 = []
while single_player != "King":
    
    system('clear')
    single_player = throw_card_prompt()
    if single_player in card_values:  
        print("you have chosen a card")
    # elif single_player == "2":
    #     print("you have chosen 2")    
    # elif single_player == "3":
    #     print("you have chosen 3")
    # elif single_player == "5":
    #     print("you have chosen 5")
    # elif single_player == "8":
    #     print("you have chosen 8")
    elif single_player == "King":
        continue
    else: 
        print("That's not a valid option!")
    input("press Enter to continue...")
    system('clear')
print("You have chosen to skip the challenge")

        
        
   








