from os import system
from players import Player, number_of_players
from player_turn import player_turn, players_threw, players_threw_clear
from list_of_challenges import which_challenge, score, value
from instructions import instructions
from card_values import card_values
from bridge import sum_of_inputs
from clear_last import clear_last
from penalty import combine_matching, get_penalty

count = 0
value_of_same = []
Score = []
def multi_player_mode():
    sum_of_same = []
    global count
    count +1
    system('clear')
    instructions()
    list_of_inputs = []
    for index in range(len(number_of_players())+1):
        if count >= (len(which_challenge())):
            if sum(Score) > 0:
                print()
                print(f"Congratulations! You scored {sum(Score)} points!!!")
                enter_high_score()
                break
            else:
                print()
                print("I'm sorry, you failed all of the challenges, better luck next time.")
                break
        elif count <=(len(which_challenge())):
            if index == 0:
                print()
                print(f"Round:{count+1}")
                print (which_challenge()[count])
                print()
                print (number_of_players()[0])
                print()
                player_turn()
                if "king" in players_threw:
                    players_threw_clear()
                    count +=1
                    multi_player_mode()
                    return None
                else: 
                    list_of_inputs.append(players_threw[0])
            elif index == 1:
                system('clear')
                instructions()
                print()
                print(f"Round:{count+1}")
                print (which_challenge()[count])
                print()
                print (number_of_players()[1])
                print()
                player_turn()
                if "king" in players_threw:
                    players_threw_clear()
                    count +=1
                    multi_player_mode()
                    return None
                else:
                    list_of_inputs.append(players_threw[1])
            elif index == 2:
                system('clear')
                instructions()
                print()
                print(f"Round:{count+1}")
                print (which_challenge()[count])
                print()
                print (number_of_players()[2])
                print()
                player_turn()
                if "king" in players_threw:
                    players_threw_clear()
                    count +=1
                    multi_player_mode()
                    return None
                else:
                    list_of_inputs.append(players_threw[2])
            elif index >= 3:   
                if([list_of_inputs[0]]*len(list_of_inputs) != list_of_inputs):
                    sum_of_inputs.append(list_of_inputs)
                    print()
                    print("You didn't reach a consensus. Please try again.") 
                    input("Press Enter to Continue...")
                    players_threw_clear()
                    multi_player_mode()
                elif([list_of_inputs[0]]*len(list_of_inputs) == list_of_inputs):
                    sum_of_inputs.append(list_of_inputs)
                    value_of_same.append(list_of_inputs[0])
                    sum_of_same.append(list_of_inputs[0])
                    sum_of_same = combine_matching(sum_of_same)
                    penalty = get_penalty(sum_of_same)
                    print()
                    input("You've reached a consensus! Press Enter to see if you succeeded in the challenge...")
                    if(card_values[value_of_same[0]] >= value()[count]):
                        print()
                        print("Congratulations! You did it!!!")
                        Score.append(score()[count] + penalty)
                        print(f"You scored {score()[count] + penalty } points")
                        input("Press Enter to Continue...")
                        value_of_same.clear()
                        players_threw_clear()
                        clear_last(sum_of_inputs)
                        count +=1
                        multi_player_mode()
                    else:
                        print()
                        print("You've failed the challenge! Keep this up and your group won't survive for long!!!")
                        input("Press Enter to Continue...")
                        value_of_same.clear()
                        players_threw_clear()
                        clear_last(sum_of_inputs)
                        count +=1
                        multi_player_mode()
    count = 0
def enter_high_score():
    print()
    name=input("Please Enter You Name: ")
    file=open("score.txt", "a")
    if sum(Score)<100000 and sum(Score)>9999: 
        file.write( "0"+ str(sum(Score)) +"\t" +(name)+ "\n")
    elif sum(Score)<10000 and sum(Score)>999: 
        file.write( "00"+ str(sum(Score)) +"\t" +(name)+ "\n")
    elif sum(Score)<1000 and sum(Score)>99: 
        file.write( "000"+ str(sum(Score)) +"\t" +(name)+ "\n")
    elif sum(Score)<100 and sum(Score)>9: 
        file.write( "0000"+ str(sum(Score)) +"\t" +(name)+ "\n")
    elif sum(Score)<10: 
        file.write( "00000"+ str(sum(Score)) +"\t" +(name)+ "\n")
    else: print("You've scored off the board you're so good!")    
        
    file.close()
    Score.clear()
    

    file=open("score.txt", "r")
    readthefile = file.readlines()
    sorted_scores = sorted(readthefile,reverse=True)

    print("Top 5 Scores! \n")
    print("Pos\tPoints\tName\n")

    for line in range(5):
        print(" " + str(line+1)+"\t"+str(sorted_scores[line]))






