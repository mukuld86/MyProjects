# Program to check if a number is prime or not
def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


x = int(input("Enter a number: "))
if prime(x):
    print("Number is a Prime Number")
else:
    print("Number is not a Prime Number")
