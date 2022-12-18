from colored import fg, attr, fore, style
green = fg('#32CD32')
res = attr('reset')
def open_high_scores():    
    
    file=open("score.txt", "r")
    readthefile = file.readlines()
    sorted_scores = sorted(readthefile,reverse=True)

    print(fore.GREEN_YELLOW + style.BOLD + "Top 5 Scores! \n")
    print(fore.GREEN_YELLOW + style.BOLD + "Pos\tPoints\tName\n")

    for line in range(5):
        print(green + " " + str(line+1)+"\t"+str(sorted_scores[line]))
