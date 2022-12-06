from os import system

# game intro - maybe include some ascii art if I have time

def game_intro():
    print("GRAaWHHH, Welcome to the Zombie Apocalypse!")
    print("     _____""\n""   _( O o )_""\n""  //\  0  /\\\\""\n"" //  |   |  \\\\""\n""(\")   | |   (\")""\n""      | |""\n""     /   \\""\n""   __|    |__")
    print("")
    opt = input("Press Enter to continue...")
    return opt

# prints the game menu with options for play vs the computer/ play vs friends / high score / Quit Game

def menu_options():
    print(" ______        __        ____      ____") 
    print("|____  /      /  \      |  _  \   |  _  \\")
    print("    / /      / /\ \     | |_| |   | |_| |")
    print("  / /__     / ____ \    |  ___/   |  ___/")
    print("/______|   /_/    \_\   |_|       |_|")
    print("")
    print("This is ZAPP - Zombie Apocalypse Planning Poker")
    print("")
    print("1. Play with the computer")
    print("2. Play with friends")
    print("3. Rules")
    print("4. High Scores")
    print("5. Quit Game")
    opt = input("Select your option (1-4): ")
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
        print("Single Player Game")
    elif option == "2":
        print("Multiplayer Game")
    elif option == "3":
        print("Rules")
    elif option == "4":
        print("High Scores")
    elif option == "5":
        continue
    else:
        print("It's not a tumor!")
    input("press Enter to continue...")
    system('clear')

print("See you on the other side, survivor!")