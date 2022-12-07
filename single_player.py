from os import system
from list_of_challenges import challenge1, challenge2, challenge3
from throw_card_prompt import throw_card_prompt

number_of_players = 3
single_player = ""

while single_player != "King":
    
    system('clear')
    single_player = throw_card_prompt()
    
   
    if single_player == "Ace" | "2" | "3" | "5" | "8" | "King":
        
        pass






