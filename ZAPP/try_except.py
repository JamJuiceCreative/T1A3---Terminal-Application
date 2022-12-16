from colored import fg, attr, fore, style
green = fg('#32CD32')
res = attr('reset')

def try_except():
    try:
        int(input(green +"Enter your name: "))
        print(green+ "Almost got you!!! To a zombie you're just a number! Number of people he's chewed on....")
    except ValueError:
            file = open("ascii_zomb.txt", "r")
            print(fore.GREEN_YELLOW + style.BOLD +file.read())
            file.close

