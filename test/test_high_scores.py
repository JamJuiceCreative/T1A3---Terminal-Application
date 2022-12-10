def open_high_scores():    
    
    print ("High Scores: \n")

    high_scores = open("test_high_scores.txt", "r")
    print(high_scores.read())
    high_scores.close()
   
