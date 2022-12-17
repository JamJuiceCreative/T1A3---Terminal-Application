thrown_cards = ["ace", "ace", "5"]


def remove_duplicates(x):
    return list(dict.fromkeys(x))
thrown_cards_unique = remove_duplicates(thrown_cards)
print("The unique Cards:", thrown_cards_unique)


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
    print("This puts the thrown cards in order:",card_index2)
    sorted_cards = sorted(card_index2.items(), key=lambda x:x[1])
    print("This converts it to a list of tuples:", sorted_cards)
    sorted_cards_slice = sorted_cards[1:-1]
    print("This removes the outside numbers",sorted_cards_slice)

    resultDictionary = dict((x, y) for x, y in sorted_cards_slice)
    print("This converts it back to a dictionary:", resultDictionary)

    card_range = {i:j for i,j in card_index2.items() if i not in resultDictionary}

    print("This gives the outside cards: ", card_range)

    card_tuple = sorted(card_index.items(), key=lambda x:x[1])
    print("This converts the original card index to a list of tuples",card_tuple)


    index_list = list(card_index)
    print("This converts card_index to a list:",index_list)

    outside_list = list(card_range)
    print("This prints the outside numbers by index:",outside_list[0], outside_list[1])

    card_range1= index_list.index(outside_list[0])
    print("This prints the index of the first outside value:",card_range1)

    card_range2= index_list.index(outside_list[1])
    print("This prints the index of the second outside value:",card_range2)

    remaining_cards = card_tuple[card_range1:card_range2+1]
    print("This give the list of remaining cards, inclusive of the outside cards:",remaining_cards)



