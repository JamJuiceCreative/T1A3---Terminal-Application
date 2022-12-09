def test_my_list(): 
    my_list = [1, 2, 3, 3]
    assert my_list[2] == my_list[3]
        

test_my_list()

# Python program to check if all
# elements in a List are same
lst = ["item","item","item","item"]
if([lst[0]]*len(lst) != lst):
    print("Equal")
   
else:
    print("Not equal")


print(len(lst))
print([lst[0]])
print([lst[0]]*len(lst))
print(lst)