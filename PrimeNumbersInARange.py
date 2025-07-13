# Write a program to print all the prime numbers for a given range given by the user (n to m)

# Under Progress
n = int(input("Enter 1st Number: "))
m = int(input("Enter 2nd Number: "))

for i in range(n, m + 1):
        if m % i == 0:
            continue
        else:
            print(i, end=" ")
