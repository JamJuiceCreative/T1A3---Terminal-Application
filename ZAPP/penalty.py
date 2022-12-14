

card_values={
        "ace": 50,
        "2": 100,
        "3": 150,
        "5": 250,
        "8" : 400
    }

# print(card_values["ace"])

sum_of_same = ["ace", "ace", "ace"]


# list_of_inputs = list(dict.fromkeys(list_of_inputs))
# print(list_of_inputs)



def combine_matching(x):
  return list(dict.fromkeys(x))



def get_penalty(x):
    return (-abs(card_values[x[0]]))
# print(list_of_inputs)

