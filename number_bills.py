""" Spicy 2: Fix the Errors """
def number_bills_needed(cost):
   num_twenty = cost // 20
   cost = cost - num_twenty * 20
   num_five = cost // 5
   cost = cost - num_five * 5
   num_one = cost // 1
   cost = cost - num_one * 1
   return num_twenty, num_five,  num_one
   
print(number_bills_needed(42))
print(number_bills_needed(17))
print(number_bills_needed(79))
print(number_bills_needed(4))
print(number_bills_needed(5))

# """ Spicy Test 2 """
# def test_number_bills_needed():
#     print("Testing number_bills_needed...", end="")
#     assert(number_bills_needed(42) == 2 + 0 + 2)
#     assert(number_bills_needed(17) == 0 + 3 + 2)
#     assert(number_bills_needed(79) == 3 + 3 + 4)
#     assert(number_bills_needed(4) == 0 + 0 + 4)
#     assert(number_bills_needed(5) == 0 + 1 + 0)
#     print("... done!")

# def test_all():
#     test_nth_fibonacci_number()
#     test_number_bills_needed()

# if __name__ == '__main__':
#     test_all()