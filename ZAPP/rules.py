from colored import fg, attr, fore, style
green = fg('#32CD32')
res = attr('reset')

def open_rules():    
    try:
        file = open("rules.txt", "r")
        print(green+file.read())
    finally:
        file.close
