import random
# assign values of cards able to be thrown
def random_card():
    card_values = ["Ace", "1" ,"2" ,"3" ,"5" ,"8" , "King"]
    # create random number generator
    def throw_card():
        return(random.sample(card_values, k=1))
        
        
    return("".join(throw_card()))


