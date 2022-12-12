# def test_random_function():

#     count=0
#     def add_numbers(num1, num2):
#         global count
#         return num1 + num2
    
#     add_numbers(2,2)

    

#     assert add_numbers(2,2) ==4

count=0

def add_numbers(num1, num2):
    global count
    count+=1
    print( num1 + num2)

add_numbers(2,2)
add_numbers(2,3)
add_numbers(2,4)

print(count)

del add_numbers

print(count)



