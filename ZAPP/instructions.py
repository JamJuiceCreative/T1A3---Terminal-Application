from colored import fg, attr, fore, style
green = fg('#32CD32')
res = attr('reset')
def instructions():
        
    print("Throw a " + fore.GREEN_YELLOW + style.BOLD + "card " + green + "either " + fore.GREEN_YELLOW + style.BOLD + "Ace, 2, 3, 5, 8 or " + fore.GREEN_YELLOW + style.BOLD + "King, " + green + "Ace being task is easy to 8 being task is hard. " + fore.GREEN_YELLOW + style.BOLD + "Throw a King " + green + "and automatically " + fore.GREEN_YELLOW + style.BOLD + "skip " + green + "the challenge.")


instructions()

