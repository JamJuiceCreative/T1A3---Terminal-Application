
def test_survivors():

    survivor1 = ["King"]
    survivor2 = [2]
    survivor3 = [2]

    assert survivor2 == survivor3

list_of_inputs = ["8", "9", "8"]

def test_while_loop():

    while ([list_of_inputs[0]]*len(list_of_inputs) == list_of_inputs):
        print ("this is a test")
    print ("those bad boys don't match")

test_while_loop()