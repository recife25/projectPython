""" Question 3: find_root """
def find_root(a, b, c):
   root_calculation = (-b+(b**2-4*a*c)**0.5)/(2*a)
   #root_calculation = (-b+((b**2)-4*a*c)**0.5/(2*a))
   return root_calculation
print(find_root(1, -7, 10))
print(find_root(1, 0, -9))
print(find_root(10, -29, -21))
print(find_root(1, -2, 1))



# """ Test 3 """
# def test_find_root():
#     import math # we use math.isclose to compare floats
#     print("Testing find_root...", end="")
#     assert(math.isclose(find_root(1, -7, 10), 5))
#     assert(math.isclose(find_root(1, 0, -9), 3))
#     assert(math.isclose(find_root(10, -29, -21), 3.5))
#     assert(math.isclose(find_root(1, -2, 1), 1))
#     print("... done!")
