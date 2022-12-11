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

thrown_cards = ["ace", "5", "8"]

del card_index2[thrown_cards[0]]
del card_index2[thrown_cards[1]]
del card_index2[thrown_cards[2]]

card_index2 = {i:j for i,j in card_index.items() if i not in card_index2}
print(card_index2)
sorted_cards = sorted(card_index2.items(), key=lambda x:x[1])

sorted_cards_slice = sorted_cards[1:-1]

print(sorted_cards)
print(type(sorted_cards[0]))
print(sorted_cards_slice)


inputTuple = sorted_cards_slice
print("The input Tuple:", inputTuple)
resultDictionary = dict((x, y) for x, y in inputTuple)
print("The result dictionary:", resultDictionary)

card_range = {i:j for i,j in card_index2.items() if i not in resultDictionary}

print("The outside cards: ", card_range)


# input tuple
inputTuple = [('ace', 0), ('5', 3), ('8', 4)]
print("The input Tuple:", inputTuple)

# Here we are iterating through each element (pairs) of the tuple using dictionary comprehension and converting it to the dictionary
resultDictionary = dict((x, y) for x, y in inputTuple)
print("The result dictionary:", resultDictionary)

a_dictionary = {"a": 1, "b": 2}
values = a_dictionary. values()
values_list = list(values)
a_value = values_list[0]
print(a_value)

card_index={
            "ace": 0,
            "2": 1,
            "3": 2,
            "5": 3,
            "8" : 4,
            "king": 5
        }
card_tuple = sorted(card_index.items(), key=lambda x:x[1])
# card_tuple = card_tuple[1:4]
print(card_tuple)
[('ace', 0), ('5', 3), ('8', 4)]

index = card_tuple.index(('ace',0))
print(index)
# card_range1 = list(card_index).index(index1)

# animals = ['cat', 'dog', 'rabbit', 'horse']

# # get the index of 'dog'
# index = animals.index('dog')


# print(index)

# # Output: 1

card_index={
            "ace": 0,
            "2": 1,
            "3": 2,
            "5": 3,
            "8" : 4,
        }

index_list = list(card_index)
# print(index_list)

outside_list = list(card_range)
print(outside_list[1])

card_range1= index_list.index(outside_list[0])
print(card_range1)

card_range2= index_list.index(outside_list[1])
print(card_range2)

remaining_cards = card_tuple[card_range1:card_range2+1]
print(remaining_cards)

print(outside_list)