from colored import fore, style, fg, attr
from player_turn import players_threw
from throw_card import random_card
from players import number_of_players
from card_values import card_values
green = fg('#32CD32')
res = attr('reset')


count = 0

def random_player_turn():
    global count
    count+=1


    single_player = ""
    if count >= len(number_of_players()):
        count = 1
    while single_player != "king": 
        
        player_threw = []
        single_player = random_card()
        if single_player == "king":
            player_threw.append(single_player)
            input(fore.GREEN_YELLOW + style.BOLD + f"{number_of_players()[count]} has voted to skip the challenge. Press Enter to Confirm..." + green)
            count+=1
            continue
        elif single_player in card_values:
            player_threw.append(single_player)
            input((fore.GREEN_YELLOW + style.BOLD + f"{number_of_players()[count]} threw {player_threw[0].capitalize()}. Press Enter to Confirm..."+ green))  
            break
        else:
            input(fore.RED + style.BOLD +"Not a valid selection. " + fore.GREEN_YELLOW + style.BOLD + "Press Enter to Continue...")
    players_threw.append(player_threw[0])

def players_threw_clear():
    players_threw.clear()



        
 









