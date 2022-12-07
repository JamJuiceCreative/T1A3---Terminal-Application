from os import system
# from list_of_challenges import challenge1, challenge2, challenge3
# from throw_card_prompt import throw_card_prompt

from player_turn import player_turn

def player1():
    system('clear')
    print("Survivor 1")
    print(input(player_turn()))
    
    

player1()