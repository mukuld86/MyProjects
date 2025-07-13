# Defining and calling a function
"""
def helloworld():
     A function to print certain Strings
    print("Hello World!")
    print("Good Morning")
    print("Have a nice day")
    print("The functon ends")

helloworld()
"""

a = int(input())
b = int(input())


def add(x, y):
    """#This functions gives the sum of the two numbers as output"""
    addition = x + y
    print(addition)


add(a, b)
print(add.__doc__)


def sub(x, y):
    """This functions gives the difference of the two numbers as output"""
    diff = x - y
    print(diff)


sub(a, b)
print(sub.__doc__)


def mul(x, y):
    """This functions gives the product of the two numbers as output"""
    prod = x * y
    print(prod)


mul(a, b)
print(mul.__doc__)
