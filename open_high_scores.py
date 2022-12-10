def open_high_scores():    
    
    file=open("score.txt", "r")
    readthefile = file.readlines()
    sorted_scores = sorted(readthefile,reverse=True)

    print("Top 5 Scores! \n")
    print("Pos\tPoints\tName\n")

    for line in range(5):
        print(" " + str(line+1)+"\t"+str(sorted_scores[line]))
