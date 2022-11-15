#find the distance between two points 
#return the calculated distance
#pothagoren theory - return hypotenuse
def distance(x1, y1, x2, y2):
    #side_length1 = abs(x2-x1)
    side_lenght1 = (x2-x1)
    side_length2 = (y2-y1)
    hypotenuse = (side_length1**2 + side_length2**2)**0.5
    return hypotenuse

print(distance(1, 1, 4, 5))
print(distance(1, 1, 1, 1))
print(distance(1, 1, 1, 3))
print(distance(2, 3, 4, 5))
print(distance(4, 5, 4, 6))
