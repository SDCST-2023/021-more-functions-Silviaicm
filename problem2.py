#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""

import math
def triangle(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    cool = [a,b,c]
    cool.sort()
    d = cool[0]
    e = cool[1]
    f = cool[2]
    if d + e <= f:
        print(0)
        return 0
    elif (d ** 2) + (e ** 2) == (f ** 2):
        print("2")
        return 2
    elif (d ** 2) + (e ** 2) < (f ** 2):
        print("3")
        return 3
    elif d != e and d != f:
        return 1
    else:
        return 0

def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  


if __name__== "__main__":
    tests()
