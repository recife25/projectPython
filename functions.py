#1.3 function 
''' Write a function called triple that takes in one parameter, n, which you can assume is an int or float, and returns three times that value.
For example,
- print(triple(5)) should print out 15
- print(triple(3.4)) should print out 10.2
- print(triple(0.0)) should print out 0.0 '''

def triple(n):
    y = n*3
    return y
print(triple(5))

def greet(name, msg):
    """This function greets to
    the person with the provided message"""
    print("Hello", name + ', ' + msg)

greet("Monica", "Good morning!")

def triple(n):
    y = n*3
    return y
print(triple(3.4))  

def triple(n):
    y = n*3
    return y
print(triple(0.0))        

''' Write a function called sum_abs_value that takes in three numbers, x, y, and z, and returns the sum of the absolute values of the numbers.
For example,
- print(sum_abs_value(1, 2, 3)) should print out 6
- print(sum_abs_value(-3, 5, 1)) should print out 9
- print(sum_abs_value(-4, -4, -2)) should print out 10 '''

# def sum_abs_value(x,y,z):
#     abs(x)
#     abs(y)
#     abs(z)
#     sum = abs(x) + abs(y) + abs(z)
#     return sum
# print(sum_abs_value(1, 2, 3))
def sum_abs_value(x,y,z):
    sum = (x+y+z)
    sum = abs(sum)
    return sum
print(sum_abs_value(1, 2, 3))

def sum_abs_value(x,y,z):
    # sum = (x+y+z)
    # sum = abs(sum)
    sum = abs(x) + abs(y) + abs(z)
    return sum
print(sum_abs_value(-3,5,1))

def sum_abs_value(x,y,z):
    sum = (x+y+z)
    sum = abs(sum)
    return sum
print(sum_abs_value(-4,-4,-2))