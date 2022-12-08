# from game_menu import game_intro

from challenges import challenges

def number_of_challenges():
    challenge1 = challenges("There's a survivor surrounded by a horde at the downtown mall", 250, False )
    challenge2 = challenges("There's an overturned supply truck on highway 99", 250, False)
    challenge3 = challenges("There's military personnel shooting innocent survivors in the city central hospital", 500, False)

    challenge_list = [challenge1.challenge, challenge2.challenge, challenge3.challenge]

    return (challenge_list)




