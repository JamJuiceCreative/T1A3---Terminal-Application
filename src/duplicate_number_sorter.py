from bridge import sum_of_inputs, remaining_cards_values

def remove_duplicates(x):
    return list(dict.fromkeys(x))
    
def get_unique_cards():
    thrown_cards = sum_of_inputs[-1]
    thrown_cards_unique = remove_duplicates(thrown_cards)
    return thrown_cards_unique


def duplicate_card_sorter():

    card_index={
                "ace": 0,
                "2": 1,
                "3": 2,
                "5": 3,
                "8" : 4,
            }

    card_index2={
                "ace": 0,
                "2": 1,
                "3": 2,
                "5": 3,
                "8" : 4
            }

    del card_index2[get_unique_cards()[0]]
    del card_index2[get_unique_cards()[1]]
  
        


    card_index2 = {i:j for i,j in card_index.items() if i not in card_index2}
    sorted_cards = sorted(card_index2.items(), key=lambda x:x[1])
    sorted_cards_slice = sorted_cards[1:-1]
    resultDictionary = dict((x, y) for x, y in sorted_cards_slice)
    card_range = {i:j for i,j in card_index2.items() if i not in resultDictionary}
    card_tuple = sorted(card_index.items(), key=lambda x:x[1])
    index_list = list(card_index)
    outside_list = list(card_range)
    card_range1= index_list.index(outside_list[0])
    card_range2= index_list.index(outside_list[1])
    remaining_cards = card_tuple[card_range1:card_range2+1]
    remaining_cards_dict = dict((x,y) for x, y in remaining_cards)
    remaining_cards_list = list(remaining_cards_dict)
    return (remaining_cards_list)

def append_remaining_card_values(x):
    remaining_cards_values.append(duplicate_card_sorter())
    return x

# append_remaining_card_values(remaining_cards_values)

# print(remaining_cards_values)
