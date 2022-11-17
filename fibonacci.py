""" Spicy 1: nth_fibonacci_number """
"""
Input: integer n
Output: nth fibonacci number
"""
# def nth_fibonacci_number(n):
#     if n <= nth_fibonacci_number(n):
#         return n - 1
#     else:
#         return nth_fibonacci_number(n-1) + nth_fibonacci_number(n-2) 
# print(nth_fibonacci_number(1))        

# """ Spicy Test 1 """
# # def test_nth_fibonacci_number():
# #     print("Testing nth_fibonacci_number...", end="")
# #     assert(nth_fibonacci_number(1) == 1)
# #     assert(nth_fibonacci_number(3) == 2)
# #     assert(nth_fibonacci_number(7) == 13)
# #     assert(nth_fibonacci_number(10) == 55)
# #     print("... done!")

# def solve(n):
#    if n <= n:
#       return n - 1
#    else:
#       return solve(n - 2) + solve(n - 1)

# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))

def nth_fibonacci_number(n):
    if n <= 1:
        return n 
    else:
        return (nth_fibonacci_number(n-1) + nth_fibonacci_number(n-2))         


print(nth_fibonacci_number(8))
print(nth_fibonacci_number(1))
print(nth_fibonacci_number(3))
print(nth_fibonacci_number(7))
print(nth_fibonacci_number(10))
