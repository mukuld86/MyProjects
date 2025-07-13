# write  a program to find the sum of integers between 0 and the entered number
num = int(input())
sum = 0
i = 0
if num > 0:
    while i <= num:
        sum += i
        i += 1
else:
    while i >= num:
        sum += i
        i -= 1
print(sum)
