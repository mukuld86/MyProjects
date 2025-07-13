""" Write a program to find the area of a circle
import math
help(math)
help(math.pow)
radius ** 2 = math.pow(radius, 2)

"""
import math
radius = int(input("Enter radius of circle"))
area = 3.14 * math.pow(radius, 2)
print("Area is ", area)

"""
OR
radius = int(input("Enter radius of circle"))
area = 3.14 * (radius ** 2)
print(area)
"""