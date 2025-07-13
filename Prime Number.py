# Program to check if a number is prime or not
n = int(input("Enter Number"))
i = 2
while i <= (n-1):
    if n % i == 0:
       print("Not Prime")
       break
    i += 1
else:
    print("Prime")
