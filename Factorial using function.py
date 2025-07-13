# WAP to find factorial of a no. using function


def factorial(x):
    i = 1
    fact = 1
    while i <= x:
        fact *= i
        i += 1
    return fact


a = int(input())
print(factorial(a))
