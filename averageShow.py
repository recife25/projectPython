#averageShow.py
""" Question 1: average_and_show_work """
"""
Inputs: three integers
Output: print out the calculation of the average of these three integers
        returns nothing
    # return result
    # print(average_and_show_work(x, y, z), str(result))
    print("("+ str(x), "+" , str(y), "+", str(z)+ ')', '/', str(3.0), '=', str(result), '/', str(3.0), '=',  result)
"""
def average_and_show_work(x, y, z):
    sum_three_number = (x + y + z) 
    avg_three_parameter = sum_three_number/3.0
    result = round (avg_three_parameter,2)
    return None
    print("("+ str(x), "+", str(y), "+", str(z) + ")", "/",  str(3), "=",  str(sum_three_number), "/", str(3), "=", result)
    
    # avg_three_parameter = (x + y + z) / 3
    # return avg_three_parameter
print(average_and_show_work(2,2,2))   
print(average_and_show_work(5,7,11)) 
print(average_and_show_work(30,-17,0)) 
""" Test 1 """
def test_average_and_show_work():
    print("Testing average_and_show_work...")
    # Check whether each call prints the expected text
    assert(average_and_show_work(2, 2, 2) == None) # (2 + 2 + 2) / 3 = 6 / 3 = 2.0
    assert(average_and_show_work(5, 7, 11) == None) # (5 + 7 + 11) / 3 = 23 / 3 = 7.67
    assert(average_and_show_work(30, -17, 0) == None) # (30 + -17 + 0) / 3 = 13 / 3 = 4.33
    print("... done!")



    #print("(", str(x), "+",  str(y), "+",  str(z),  ")", "/",  str(3.0), "=",  str(result), "/",  str(3.0), "=",  result)