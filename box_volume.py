""" Question 1: box_volume """
"""
Inputs: three integers representing the height, width, and length of a box
Output: the volume of the box
"""
def box_volume(h, w, l):
    box_volume_formula = (h*w*l)
    return box_volume_formula
print(box_volume(3, 4, 2)) 
print(box_volume(2, 2, 2))
print(box_volume(5, 2, 0))


# """ Test 1 """
# def test_box_volume():
#     print("Testing box_volume...", end="")
#     assert(box_volume(3, 4, 2) == 24)
#     assert(box_volume(2, 2, 2) == 8)
#     assert(box_volume(5, 2, 0) == 0)
#     print("... done!")
