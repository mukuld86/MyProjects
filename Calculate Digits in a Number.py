# Write a program to find number of digits in a number
a = int(input("Enter a number: "))
c = 0
while a > 0:
    a = a//10
    c += 1
print(c)
"""
OR
a = int(input("Enter a number: "))
b = str(a)
print(len(b))
"""