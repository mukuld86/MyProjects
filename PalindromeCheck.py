# write a program to check if a number is palindrome or not. Palindrome=
n = int(input("Enter a number:"))
temp = n
r = 0
while a > 0:
    d = n % 10
    r = r * 10 + d
    n = n // 10
print(r)
if temp == r:
    print("Number is palindrome")
else:
    print("Number is not palindrome")
