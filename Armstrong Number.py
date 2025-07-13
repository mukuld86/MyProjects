#Write a program to check if a number is an armstrong number or not

n=int(input("Enter a number: "))
p=len(str(n))
temp=n
r=0
sum=0
while n>0:
    d=n%10
    sum+=(d**p)
    r=10*r+d
    n=n//10
if sum==temp:
    print(temp,"is an armstrong number.")
else:
    print(temp,"is not an armstrong number.")
