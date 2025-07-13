# Write a program to find the LCM of two numbers
a = int(input())
b = int(input())
if a > b:
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            print(i)
            break
elif b > a:
    for i in range(2, b + 1):
        if a % i == 0 and b % i == 0:
            print(i)
            break
else:
    for i in range(2, a + 1):
        if a % i == 0:
            print(i)
            break
