from utils.players import number_of_players



def test_round_checker():
    sum_of_inputs = [["King", "Ace", "2"],["King", "Ace", "2"],["King", "Ace", "2"]]
    assert (len(sum_of_inputs))==(len(number_of_players()))
    print(len(sum_of_inputs))
    print(round)

test_round_checker()