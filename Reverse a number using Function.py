def pal(n):
    r = 0
    temp = n
    while n > 0:
        d = n % 10
        r = r * 10 + d
        n = n // 10
    if temp == r:
        print("Palindrome")
    else:
        print("Not Palindrome")


a = int(input("Enter a number: "))
pal(a)
pal(2 * a)
