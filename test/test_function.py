def test_functions():   
    
    
    def test_say_hello(greeting):
        print(greeting)

    test_say_hello("hello")

    def test_say_hello(greeting):
        print(greeting)

    test_say_hello("hello again")

list = []

def test_say_hello():
    return("hello")

list.append(test_say_hello())

n = [3,5,7]
#function goes here
def myFun(x):
    n.append(test_say_hello())
    return x
print (myFun(n))