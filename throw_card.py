import random
from player_turn import players_threw
from players import number_of_players

count = 1
# assign values of cards able to be thrown
def random_card():
    global count
    count +1
    if count != len(number_of_players()):
        card_values = ["ace", "2" ,"3" ,"5" ,"8" , "king"]
        # create random number generator
        def throw_card():
            return(random.sample(card_values, k=1))
    else:
        card_values = ["Mad" ,"Hatter" ,"is" ,"coming"]
        def throw_card():
            return(random.sample(card_values, k=1))     
        
    return("".join(throw_card()))


