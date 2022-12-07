

def test_card_values():
    card_values={
        "Ace": 50,
        1: 100,
        2: 250,
        5: 500,
        8: 750,
        "king": 1000
    }

    single_player = 2

    assert(single_player in card_values)

