""" Question 2: make_introduction """
"""
Inputs: two strings representing a name and a hobby
Output: a string of the form "My name is {name} and I like {hobby}"
"""
def make_introduction(name, hobby):
    test_make_introduction = ("My name is " + name + " and I like " + hobby)
    return test_make_introduction
print(make_introduction("Nnenna", "swimming"))
    
    

# """ Test 2 """
# def test_make_introduction():
#     print("Testing make_introduction...", end="")
#     assert(make_introduction("Nnenna", "swimming") == "My name is Nnenna and I like swimming")
#     assert(make_introduction("Sigurd", "cooking") == "My name is Sigurd and I like cooking")
#     assert(make_introduction("Rei", "reading") == "My name is Rei and I like reading")
#     assert(make_introduction("Govind", "dancing") == "My name is Govind and I like dancing")
#     print("... done!")