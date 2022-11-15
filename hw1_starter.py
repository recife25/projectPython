""" Question 1: box_volume """
"""
Inputs: three integers representing the height, width, and length of a box
Output: the volume of the box
"""
def box_volume(h, w, l):
    return

""" Test 1 """
def test_box_volume():
    print("Testing box_volume...", end="")
    assert(box_volume(3, 4, 2) == 24)
    assert(box_volume(2, 2, 2) == 8)
    assert(box_volume(5, 2, 0) == 0)
    print("... done!")


""" Question 2: make_introduction """
"""
Inputs: two strings representing a name and a hobby
Output: a string of the form "My name is {name} and I like {hobby}"
"""
def make_introduction(name, hobby):
    return

""" Test 2 """
def test_make_introduction():
    print("Testing make_introduction...", end="")
    assert(make_introduction("Nnenna", "swimming") == "My name is Nnenna and I like swimming")
    assert(make_introduction("Sigurd", "cooking") == "My name is Sigurd and I like cooking")
    assert(make_introduction("Rei", "reading") == "My name is Rei and I like reading")
    assert(make_introduction("Govind", "dancing") == "My name is Govind and I like dancing")
    print("... done!")


""" Question 3: find_root """
"""
Inputs: three integers a, b, c
Output: the positive quadratic root of the equation ax^2 + bx + c = 0
        (using the quadratic formula)
"""
def find_root(a, b, c):
    return

""" Test 3 """
def test_find_root():
    import math # we use math.isclose to compare floats
    print("Testing find_root...", end="")
    assert(math.isclose(find_root(1, -7, 10), 5))
    assert(math.isclose(find_root(1, 0, -9), 3))
    assert(math.isclose(find_root(10, -29, -21), 3.5))
    assert(math.isclose(find_root(1, -2, 1), 1))
    print("... done!")


""" Question 4: Fix the Syntax Errors """
"""
Uncomment the following function and fix the syntax errors so it passes
"""
#def tens_digit(n):
#    n // 10 = n
#return n % 10

""" Test 4 """
def test_tens_digit():
    print("Testing tens_digit...", end="")
    assert(tens_digit(1234) == 3)
    assert(tens_digit(42) == 4)
    assert(tens_digit(9) == 0)
    print("... done!")


""" Question 5: Fix the Runtime Errors """
def compute_total(total, tax):
    final = total + total*tax
    print("Your total is " + final + " dollars.")
    return FINAL

""" Test 5 """
def test_compute_total():
    import math # we use math.isclose to compare floats
    print("Testing compute_total...", end="")
    assert(math.isclose(compute_total(12, 0.05), 12.6))
    assert(math.isclose(compute_total(15, 0.07), 16.05))
    assert(math.isclose(compute_total(5.75, 0), 5.75))
    print("... done!")


""" Question 6: Fix the Logical Errors """
def slope(x1, y1, x2, y2):
    result = y2 - y1 / x2 - x1
    return slope

""" Test 6 """
def test_slope():
    import math # we use math.isclose to compare floats
    print("Testing slope...", end="")
    assert(math.isclose(slope(1, 3, 6, 5), 0.4))
    assert(math.isclose(slope(2, 4, 6, 8), 1))
    assert(math.isclose(slope(0, 2, 5, -2), -0.8))
    print("... done!")

def test_all():
    test_box_volume()
    test_make_introduction()
    test_find_root()
    test_tens_digit()
    test_compute_total()
    test_slope()

if __name__ == '__main__':
    test_all()