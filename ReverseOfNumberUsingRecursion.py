# Write a program to reverse a number using recursion
N = 0


def rev(n):
    global N
    if n > 0:
        r = n % 10
        N = (N * 10) + r
        rev(n // 10)
    return N
x = int(input("Enter a number: "))
print(rev(x))
