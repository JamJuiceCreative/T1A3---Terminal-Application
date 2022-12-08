from player_class import Player

def number_of_players():
    player1 = Player("Survivor 1")
    player2 = Player("Survivor 2")
    player3 = Player("Survivor 3")
 
    player_list = [player1.name, player2.name, player3.name]
   
    return (player_list)


# print(player_list)

# def creating_list():
#     return [x for x in range (6)]
# counts = creating_list()
# print(f"The returned list is: ', {counts}")


# player1 = Player("Survivor 1")
# player2 = Player("Survivor 2")
# player3 = Player("Survivor 3")

# player_list = [player1, player2, player3]

# print (player_list)

# print(player1.name)

# print(number_of_players())