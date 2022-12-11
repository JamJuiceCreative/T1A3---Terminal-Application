# from single_player import number_sorter

card_index={
        
        "2": 1,
        "3": 2,
        "5": 3,
        "ace": 0,
        "8" : 4,
        "king": 5
    }
sorted_cards = sorted(card_index.items(), key=lambda x:x[1])

print(sorted_cards)

drawn_cards= ["Ace", "3", "8"]

if drawn_cards in card_index