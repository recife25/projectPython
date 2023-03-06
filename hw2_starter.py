""" Question 1: average_and_show_work """
"""
Inputs: three integers
Output: print out the calculation of the average of these three integers
        returns nothing
"""
def average_and_show_work(x, y, z):
    avg_three_parameter = (x + y + z) / 3 
    return avg_three_parameter
print(average_and_show_work(2,2,2))   

""" Test 1 """
def test_average_and_show_work():
    print("Testing average_and_show_work...")
    # Check whether each call prints the expected text
    assert(average_and_show_work(2, 2, 2) == None) # (2 + 2 + 2) / 3 = 6 / 3 = 2.0
    assert(average_and_show_work(5, 7, 11) == None) # (5 + 7 + 11) / 3 = 23 / 3 = 7.67
    assert(average_and_show_work(30, -17, 0) == None) # (30 + -17 + 0) / 3 = 13 / 3 = 4.33
    print("... done!")


""" Question 2: random_gcd() """
"""
Inputs: None
Output: randomly generates two integers in range [1, 100] and returns gcd
"""
def random_gcd():
    return

""" Test 2 """
def test_random_gcd():
    print("Testing random_gcd...")
    # Check whether the result is actually the GCD of the two printed numbers
    result = random_gcd() # should print x and y
    print("gcd:", result) # prints the result
    print("... done!")


""" Question 3: RSA """
"""
Write three functions - encode, decode, and transmit - that transmits a message
with RSA encryption. 
"""
def encode(m, e, n):
    return

def decode(m, d, n):
    return

def transmit(message, e, d, n):
    return

""" Test 3 """
def test_rsa():
    print("Testing RSA functions...")
    # We'll test using two valid sets of RSA keys:
    # A: e = 7, d = 23, n = 697 [generated from p=17, q=41]
    # B: e = 143, d = 16427, n = 50573 [generated from p=491, q=103]
    assert(encode(402, 7, 697) == 326)
    assert(encode(213, 7, 697) == 2)
    assert(encode(1234, 143, 50573) == 42522)

    assert(decode(326, 23, 697) == 402)
    assert(decode(2, 23, 697) == 213)
    assert(decode(42522, 16427, 50573) == 1234)

    assert(transmit(402, 7, 23, 697) == 402) # prints "Transmitting: 326"
    assert(transmit(213, 7, 23, 697) == 213) # prints "Transmitting: 2"
    assert(transmit(1234, 143, 16427, 50573) == 1234) # prints "Transmitting: 42522"
    print("... done!")


""" Question 4: check_conditions """
"""
Inputs: three integers 
Output: True if at least one of the following is true:
        1. Both x and y are greater than 10
        2. Either one of y or z is odd
"""
def check_conditions(x, y, z):
    return

""" Test 4 """
def test_check_conditions():
    print("Testing check_conditions...", end="")
    assert(check_conditions(12, 14, 7) == True)
    assert(check_conditions(15, 1, 9) == True)
    assert(check_conditions(10, 12, -2) == False)
    assert(check_conditions(19, 16, 4) == True)
    assert(check_conditions(1, 3, 5) == True)
    print("... done!")


""" Question 5: estimate_shipping_time """
"""
Inputs: a month (string) and day (integer)
Output: shipping time needed to ship an item on specified date with special cases:
        1. Most items ship in 10 days
        2. December is busy so items that ship in December take 5 days longer
        3. December 25 - end of year is even busier, so items shipped then take 
           5 more days
        4. Items that ship before the 7th of the month take 3 fewer days
           (This rule doesn't apply to December)
"""
def estimate_shipping_time(month, day):
    return

""" Test 5 """
def test_estimate_shipping_time():
    print("Testing estimate_shipping_time...", end="")
    assert(estimate_shipping_time("July", 12) == 10)
    assert(estimate_shipping_time("April", 4) == 7)
    assert(estimate_shipping_time("October", 7) == 7)
    assert(estimate_shipping_time("January", 8) == 10)
    assert(estimate_shipping_time("December", 2) == 15)
    assert(estimate_shipping_time("December", 24) == 15)
    assert(estimate_shipping_time("December", 25) == 20)
    print("... done!")


""" Question 6: Debug the Function """
def fahrenheit_to_celsius(temp):
    return (temp - 32) * (5 // 9)

def is_nice_outside(temperature, in_fahrenheit, is_raining):
    if in_fahrenheit:
        temperature = farenheit_to_celsius(temperature)
    return (not is_raining) and ((temperature > 4) or (temperature < 35))

""" Test 6 """
def test_is_nice_outside():
    print("Testing is_nice_outside...", end="")
    assert(is_nice_outside(-10, False, False) == False)
    assert(is_nice_outside(72, True, True) == False)
    assert(is_nice_outside(0, False, True) == False)
    assert(is_nice_outside(69, True, False) == True)
    assert(is_nice_outside(102, True, False) == False)
    assert(is_nice_outside(5, False, False) == True)
    print("... done!")

def test_all():
    test_average_and_show_work()
    test_random_gcd()
    test_rsa()
    test_check_conditions()
    test_estimate_shipping_time()
    test_is_nice_outside()

if __name__ == '__main__':
    test_all()