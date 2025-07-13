"""
write a program to find area of circle , rectangle and square using function & return
"""
import math
r = int(input("Enter radius of circle: "))
l = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
s = int(input("Enter side of square: "))


def ca():
    a1 = math.pi * r * r
    return a1


def ra():
    a2 = l * b
    return a2


def sa():
    a3 = pow(s, 2)
    return a3


print("Area of Circle is:", "% .2f" % ca())
print("Area of Rectangle is:", ra())
print("Area of Square is:", sa())
