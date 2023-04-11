#!python3

"""
Create a function that determines the area of a circle if given the radius
1 input parameter
float: radius

return: float area for the circle

note: Area of a circle is given by A = pi*(square of the radius)
You may want to use the math module to complete this problem
"""

import math
def area(a):
    a = float(a)
    b = math.pi * (a ** 2)
    print(b)
    return b

if __name__ == "__main__":
    assert round(area(2),2) == 12.57