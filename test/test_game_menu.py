from os import system

def test_game_intro():
    print("GRAaWHHH, Welcome to the Zombie Apocalypse!")
    opt = input("Press Enter to continue...")
    return opt

intro = ""

while intro != "q":
    system('clear')
    intro = test_game_intro()