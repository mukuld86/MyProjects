# write a program to find the sum of digits of a number
n = int(input("Enter a number"))
l = list(str(n))
sum = 0
for i in l:
    a = int(i)
    sum += a
print(sum)
