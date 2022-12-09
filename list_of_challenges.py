# from game_menu import game_intro

from challenges import challenges

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




