# write a program to ask user to enter a number and print the sum of all even numbers up to that number.
a = int(input("Enter a number"))
b = 0
s = 0
if a % 2 == 0:
    while b <= a:
        s += b
        b += 2
else:
    while b <= a - 1:
        s += b
        b += 2
print(s)
