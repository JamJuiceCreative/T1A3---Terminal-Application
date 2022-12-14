from os import system
from colored import fg, attr, fore, style
from open_high_scores import open_high_scores
from rules import open_rules
from multi_player import multi_player_mode
from single_player import single_player_mode
from art import *
# game intro - maybe include some ascii art if I have time
              


green = fg('#32CD32')
green_yellow = fg ('#ADFF2F')
res = attr('reset')

       
def game_intro():
    print(fore.GREEN_YELLOW + style.BOLD + "GRAaWHHH, Welcome to the Zombie Apocalypse!" + res)
    print(green + style.BOLD +"            _____                   ""\n""          _( O o )_                 ""\n""         //\  0  /\\\\                ""\n""        //  |   |  \\\\               ""\n""       (\")   | |   (\")              ""\n""             | |                    ""\n""            /   \\                   ""\n""          __|    |__                "+ res)
    print()
    opt = input(fore.GREEN_YELLOW + style.BOLD +"Press Enter to continue...")
    return opt

# prints the game menu with options for play vs the computer/ play vs friends / high score / Quit Game

def menu_options():
    Art=text2art("Z   A   P   P") # Return ASCII text (default font) and default chr_ignore=True 
    print(Art)
    print("This is ZAPP - Zombie Apocalypse Planning Poker")
    print("")
    print(green +"1. Play with the computer")
    print("2. Play with friends")
    print("3. Rules")
    print("4. High Scores")
    print("5. Quit Game")
    print()
    opt = input(fore.GREEN_YELLOW + style.BOLD + "Select your option (1-5): ")
    return opt

intro = ""

while intro != "q":
    system('clear')
    intro = game_intro()
    if intro != "q":
        break
    else:
        exit


option = ""

while option != "5":
    system('clear')
    option = menu_options()
    system('clear')
    if option == "1":
        single_player_mode()
    elif option == "2":
        multi_player_mode()
    elif option == "3":
        open_rules()
    elif option == "4":
        open_high_scores()
    elif option == "5":
        continue
    else:
        print(green + "It's not a tumor!")
    input(fore.GREEN_YELLOW + style.BOLD + "press Enter to continue...")
    system('clear')

print(green + "See you on the other side, survivor!")

