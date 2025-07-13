"""
Write a program that demonstrates operator precedence. Take two integers a and b as input from the console.
Calculate the following expressions:
a+b*5
a+b*5*10/2
"""
a = int(input("Enter an Integer value:"))
b = int(input("Enter an Integer value:"))
print(a, "+", b, " * 5 = ", a + b * 5)
print(a, "+", b, " * 5 * 10 / 2 = ", a + b * 5 * 10 / 2)
