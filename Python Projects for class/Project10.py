#Scientific Calculator
import math
while True:
    a=float(input("num1: "))
    b=float(input("num2: "))
    print("{} + {} = {}".format( a , b , a+b ))
    print("{} - {} = {}".format( a , b , a-b ))
    print("{} * {} = {}".format( a , b , a*b ))
    print("{} / {} = {}".format( a , b , a/b ))
    print("{} % {} = {}".format( a , b , a%b ))
    print("{} square equals: {}".format( a , a**2 ))
    print("{} square equals: {}".format( b , b**2 ))
    print("{} raised to the power {} equals {}".format( a , b , math.pow(a,b) ))
    print("sin{} = {} , cos{} = {} , tan{} = {}".format(a , math.sin(a) , a , math.cos(a) , a , math.tan(a) ))
    print("sin{} = {} , cos{} = {} , tan{} = {}".format(b , math.sin(b) , b , math.cos(b) , b , math.tan(b) ))
    print("{} radians equals {} degreees.".format( a , math.radians(a) ))
    print("{} radians equals {} degreees.".format( b , math.radians(b) ))
    print("{} degrees equals {} radians.".format( a , math.degrees(a) ))
    print("{} degrees equals {} radians.".format( b , math.degrees(b) ))
    print()