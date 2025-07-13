# write a program to print fibonacci series up to n terms
n = int(input("Enter a number"))
a = 0
b = 1
temp = 0
c = 1
while c <= n:
    if a == 0:
        print(a)
        print(b)
        temp = a + b
        a = b
        b = temp
    else:
        temp = a + b
        a = b
        b = temp
        print(a)
    c += 1
