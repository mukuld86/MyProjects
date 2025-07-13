# write a program to swap 2 numbers without using 3rd variable
a = int(input("Enter number 1"))
b = int(input("Enter Number 2"))

a, b = b, a
print("Number 1 is", a)
print("Number 2 is", b)

"""
Another method to do this
a=a+b
b=a-b
a=a-b
"""