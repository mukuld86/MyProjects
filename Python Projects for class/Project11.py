import random
a=int(input("Range Initial point: "))
b=int(input("Range end point: "))
num=random.randrange(a,b)
print("Randomly generated number in the given range is",num)

#check for even or odd
if num%2==0:
    print(num,"is an even number.")
else:
    print(num,"is an odd number.")

#check for positive or negative
if num>0:
    print(num,"is a positive number.")
elif num<0:
    print(num,"is a negative number.")
else:
    pass

#now check for prime number
i=2
while(i<num):
    if num%i==0:
       res="is a composite number."
       break
    i+=1
else:
    if num==1:
        res="is a composite number."
    else:
        res="is a Prime number."
        if num<0:
            res="is not a Prime number"
print(num,res)