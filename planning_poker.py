import random
# assign values of cards able to be thrown
card_values = ["Ace", 1 ,2 ,3 ,5 ,8 , "King"]
# create random number generator
def throw_card():
    print(random.choice(card_values))
    
# print (card_values[5])

print(card_values[6])

throw_card()