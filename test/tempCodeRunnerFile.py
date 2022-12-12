def check_for_duplicates():
    thrown_cards = ["5", "4", "8"]
    def remove_duplicates(x):
        return list(dict.fromkeys(x))
    thrown_cards_unique = remove_duplicates(thrown_cards)
    if len(thrown_cards) != len(thrown_cards_unique):
        return True
print(check_for_duplicates())