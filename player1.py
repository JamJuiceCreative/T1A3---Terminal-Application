from os import system
# from list_of_challenges import challenge1, challenge2, challenge3
# from throw_card_prompt import throw_card_prompt
from player_turn import player_turn

def player1_gamertag():
    print("Survivor 1")
    player_turn()

player1 = ""

while player1 != "q":
    system('clear')
    player1 = player1_gamertag()

# def player1():
#     system('clear')
#     print("Survivor 1")
#     player_turn()
    
    
    

# player1()