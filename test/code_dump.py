# def remove_duplicates(x):
#     return list(dict.fromkeys(x))
# thrown_cards_unique = remove_duplicates(thrown_cards)
# print("The unique Cards:", thrown_cards_unique)

# if len(thrown_cards_unique) == (number_of_players()):
#     del card_index2[thrown_cards_unique[0]]
#     del card_index2[thrown_cards_unique[1]]
#     del card_index2[thrown_cards_unique[2]]
#     pass
# elif len(thrown_cards_unique)==len(number_of_players())-1:
#     thrown_cards_unique.append("100")
#     print(thrown_cards_unique) 
#     del card_index2[thrown_cards_unique[0]]
#     del card_index2[thrown_cards_unique[1]]

# index = card_tuple.index(('ace',0))
# print(index)
# card_range1 = list(card_index).index(index1)

# animals = ['cat', 'dog', 'rabbit', 'horse']

# # get the index of 'dog'
# index = animals.index('dog')


# print(index)

# # Output: 1

# card_index={
#             "ace": 0,
#             "2": 1,
#             "3": 2,
#             "5": 3,
#             "8" : 4,
#         }

# # input tuple
# inputTuple = [('ace', 0), ('5', 3), ('8', 4)]
# print("The input Tuple:", inputTuple)

# # Here we are iterating through each element (pairs) of the tuple using dictionary comprehension and converting it to the dictionary
# resultDictionary = dict((x, y) for x, y in inputTuple)
# print("The result dictionary:", resultDictionary)

# a_dictionary = {"a": 1, "b": 2}
# values = a_dictionary. values()
# values_list = list(values)
# a_value = values_list[0]
# b_value = values_list[1]

from players import number_of_players
from duplicate_number_sorter import duplicate_card_sorter
from bridge import sum_of_inputs

remaining_cards_values = []
print(remaining_cards_values)
thrown_cards = sum_of_inputs[-1]



def check_for_duplicates():
    def remove_duplicates(x):
        return list(dict.fromkeys(x))
    thrown_cards_unique = remove_duplicates(thrown_cards)
    if len(thrown_cards) != len(thrown_cards_unique):
        return True


def card_sorter():
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

    del card_index2[thrown_cards[0]]
    del card_index2[thrown_cards[1]]
    del card_index2[thrown_cards[2]]

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
    return remaining_cards_list

def run_next():

    if len(thrown_cards) == len(number_of_players()):
        check_for_duplicates()
        if check_for_duplicates() == True:
            duplicate_card_sorter()
        else:
            card_sorter()
    else:
        print("something went wrong")



remaining_cards_values.append(card_sorter())

print(remaining_cards_values)

run_next()


from bridge import sum_of_inputs

thrown_cards = sum_of_inputs[-1]


def remove_duplicates(x):
    return list(dict.fromkeys(x))
thrown_cards_unique = remove_duplicates(thrown_cards)

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

    del card_index2[thrown_cards_unique[0]]
    del card_index2[thrown_cards_unique[1]]


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
    return(remaining_cards_list)




