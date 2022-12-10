from os import system
from players import Player, number_of_players
from player_turn import player_turn, players_threw, players_threw_clear
from list_of_challenges import which_challenge, score, value
from instructions import instructions
from card_values import card_values


sum_of_inputs = []
count = 0
value_of_same = []
Score = []
def multi_player_mode():
    global count
    count +1
    system('clear')
    instructions()
    list_of_inputs = []
    for index in range(len(number_of_players())+1):
        if count >= (len(which_challenge())):
            if sum(Score) > 0:
                print(f"Congratulations! You scored {sum(Score)} points!!!")
                enter_high_score()
                # print("I'm sorry, you failed all of the challenges, better luck next time.")
                break
            else:
                # print(f"Congratulations! You scored {sum(Score)} points!!!")
                print("I'm sorry, you failed all of the challenges, better luck next time.")
                break
        elif count <=(len(which_challenge())):
            if index == 0:
                print (number_of_players()[0])
                print(f"Round:{count+1}")
                print (which_challenge()[count])
                player_turn()
                if "King" in players_threw:
                    players_threw_clear()
                    count +=1
                    multi_player_mode()
                    return None
                else: 
                    list_of_inputs.append(players_threw[0])
                    input((list_of_inputs[0]))
            elif index == 1:
                system('clear')
                instructions()
                print()
                print (number_of_players()[1])
                print(f"Round:{count+1}")
                print (which_challenge()[count])
                player_turn()
                if "King" in players_threw:
                    players_threw_clear()
                    count +=1
                    multi_player_mode()
                    return None
                else:
                    list_of_inputs.append(players_threw[1])
                    input((list_of_inputs[1]))
            elif index == 2:
                system('clear')
                instructions()
                print()
                print (number_of_players()[2])
                print(f"Round:{count+1}")
                print (which_challenge()[count])
                player_turn()
                if "King" in players_threw:
                    players_threw_clear()
                    count +=1
                    multi_player_mode()
                    return None
                else:
                    list_of_inputs.append(players_threw[2])
                    input((list_of_inputs[2]))
            elif index >= 3:
                # check if all items in list_of_inputs are the same
                
                if([list_of_inputs[0]]*len(list_of_inputs) != list_of_inputs):
                    sum_of_inputs.append(list_of_inputs)
                    input(sum_of_inputs)
                    input(list_of_inputs)
                    players_threw_clear()
                    multi_player_mode()
                elif([list_of_inputs[0]]*len(list_of_inputs) == list_of_inputs):
                    sum_of_inputs.append(list_of_inputs)
                    value_of_same.append(list_of_inputs[0])
                    if(card_values[value_of_same[0]] >= value()[0]):
                        print("You did it!!!!")
                        Score.append(score()[count])
                        input(Score)
                        print(f"You scored {score()[count]} points")
                        input(value_of_same)
                        value_of_same.clear()
                        players_threw_clear()
                        count +=1
                        multi_player_mode()
                    else:
                        print("you failed!!!")
                        input(value_of_same)
                        value_of_same.clear()
                        
                        players_threw_clear()
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

        
    



