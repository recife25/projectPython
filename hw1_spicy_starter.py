""" Spicy 1: nth_fibonacci_number """
"""
Input: integer n
Output: nth fibonacci number
"""
def nth_fibonacci_number(n):
    return

""" Spicy Test 1 """
def test_nth_fibonacci_number():
    print("Testing nth_fibonacci_number...", end="")
    assert(nth_fibonacci_number(1) == 1)
    assert(nth_fibonacci_number(3) == 2)
    assert(nth_fibonacci_number(7) == 13)
    assert(nth_fibonacci_number(10) == 55)
    print("... done!")


""" Spicy 2: Fix the Errors """
"""
Input: cost
Output: least number of $20, $5, and $1 bills needed to cover cost
"""
#def number_bills_needed(cost):
#    num_twenty = cost // 0
#    cost = cost - num_twenty * 20
#    num_five = cost // 5
#    cost = cost - num_five + 5
#    num_one = cost
#    return num_twenty + num_five + num_ one

""" Spicy Test 2 """
def test_number_bills_needed():
    print("Testing number_bills_needed...", end="")
    assert(number_bills_needed(42) == 2 + 0 + 2)
    assert(number_bills_needed(17) == 0 + 3 + 2)
    assert(number_bills_needed(79) == 3 + 3 + 4)
    assert(number_bills_needed(4) == 0 + 0 + 4)
    assert(number_bills_needed(5) == 0 + 1 + 0)
    print("... done!")

def test_all():
    test_nth_fibonacci_number()
    test_number_bills_needed()

if __name__ == '__main__':
    test_all()