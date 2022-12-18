from os import system
from colored import fore, style, fg, attr
from throw_card_prompt import throw_card_prompt
from card_values import card_values
green = fg('#32CD32')
res = attr('reset')
players_threw = []

def player_turn():
    

    single_player = ""
    
    while single_player != "king":
        player_threw = []
        single_player = throw_card_prompt()
        if single_player == "king":
            player_threw.append(single_player)
            input(fore.GREEN_YELLOW + style.BOLD +"You have voted to skip the challenge. Press Enter to Continue..." + green )
            continue
        elif single_player in card_values:
            player_threw.append(single_player)
            input((fore.GREEN_YELLOW + style.BOLD + f"You threw {player_threw[0].capitalize()}. Press Enter to Continue..." + green ))
            break
        else: 
            input(fore.RED + style.BOLD +"Not a valid selection. " + fore.GREEN_YELLOW + style.BOLD + "Press Enter to Continue...")
            
    players_threw.append(player_threw[0])
    
    

def players_threw_clear():
    players_threw.clear()






