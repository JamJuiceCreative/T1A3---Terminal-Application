import random

from bridge import sum_of_inputs
from number_sorter import run_next, remaining_cards_values


# assign values of cards able to be thrown
def random_card():
    if len(sum_of_inputs) == 1:
        card_values = ["ace", "2" ,"3" ,"5" ,"8" , "king"]
        # create random number generator
        def throw_card():
            return(random.sample(card_values, k=1))

    else:
        
        card_values_range = remaining_cards_values
        def throw_card():
            return(random.sample(card_values_range, k=1))
    print(remaining_cards_values)
    print("This is the sum of inputs:",sum_of_inputs)
    return("".join(throw_card()))
exit

