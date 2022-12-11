# # from single_player import number_sorter
# def test_number_sorter():
#     card_index={
            
#             "2": 1,
#             "3": 2,
#             "5": 3,
#             "ace": 0,
#             "8" : 4,
#             "king": 5
#         }
#     sorted_cards = sorted(card_index.items(), key=lambda x:x[1])

#     drawn_cards_dict = {}

#     print(sorted_cards)
#     drawn_cards = ["ace", "8", "3"]
#     if drawn_cards[0] in card_index.keys():
#         print (key,value)

#     # drawn_cards = ["Ace", "3", "8"]
#     # assert drawn_cards in card_index == True
# test_number_sorter()

# my_dict = {
#     'names': ['alice', 'bobbyhadz', 'carl'],
#     'tasks': ['develop', 'test', 'ship'],
#     'language': ['js', 'py', 'ts']
# }

# butts = "develop"
# print(butts)

# for key, value in my_dict.items():
#     if butts in value:
#         print(key, value)


# card_index={
            
#             "2": 1,
#             "3": 2,
#             "5": 3,
#             "ace": 0,
#             "8" : 4,
#             "king": 5
#         }
# def card_sorter():
#     for key, value in card_index.items():
#         if "ace" in key:
        
#             (key, value)

# thrown_cards_sorter = {}

# thrown_cards_sorter[card_sorter] = card_sorter



# print(card_sorter()) 
# # print(thrown_cards_sorter{})


# GOOD CODE STARTS HERE

card_index={
            "ace": 0,
            "2": 1,
            "3": 2,
            "5": 3,
            "8" : 4,
            "king": 5
        }

        

card_index2={
            "ace": 0,
            "2": 1,
            "3": 2,
            "5": 3,
            "8" : 4,
            "king": 5
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




# GOOD CODE ENDS HERE

# sorted_cards = {i:j for i,j in sorted_cards() if i not in sorted_cards_slice}
# print(sorted_cards)

# dict1 = {'ana': 'http://ted.com', 'louise': 'http://reddit.com', 'sarah':'http://time.com'}
# dict2 = {'patricia': 'http://yahoo.com', 'ana': 'http://ted.com',
#          'louise': 'http://reddit.com', 'florence': 'http://white.com'}

# dict2 = {i:j for i,j in dict2.items() if i not in dict1}

# print(dict2)

# input tuple
