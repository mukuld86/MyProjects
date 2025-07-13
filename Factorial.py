# write a program to find the factorial of an entered number

a = int(input("Enter a number: "))
f = 1
while a >= 1:
    f *= a
    a -= 1

print("Factorial: ", f)
