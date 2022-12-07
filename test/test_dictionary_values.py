def test_card_values():

    card_values={
        "Ace": 50,
        2: 100,
        3: 250,
        5: 500,
        8: 750,
        "king": 1000
    }
    
    assert("Ace" not in card_values.items())

    assert(2 in card_values)

