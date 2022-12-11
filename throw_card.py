import random
# assign values of cards able to be thrown
def random_card():
    card_values = ["ace", "2" ,"3" ,"5" ,"8" , "king"]
    # create random number generator
    def throw_card():
        return(random.sample(card_values, k=1))
        
        
    return("".join(throw_card()))


