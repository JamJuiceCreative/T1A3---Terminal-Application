from utils.challenges import challenges
from utils.card_values import card_values
challenge1 = challenges("There's a survivor surrounded by a horde at the downtown mall", 250, False, 1000 )
challenge2 = challenges("There's an overturned supply truck on highway 99", 250, False, 1000)
challenge3 = challenges("There's military personnel shooting innocent survivors in the city central hospital", 400, False, 5000)
def which_challenge():
    challenge_list = [challenge1.challenge, challenge2.challenge, challenge3.challenge]
    return (challenge_list)

def score():
    score_list = [challenge1.score, challenge2.score, challenge3.score]
    return (score_list)

def value():
    value_list = [challenge1.value, challenge2.value, challenge3.value]
    return (value_list)


print(len(which_challenge()))
print(which_challenge())

print(score())
print(card_values["5"])
print(value()[0])

def test_check_values():

    assert (card_values["5"]) == (value()[0])





