l = [0]
a = 1
b = 1
while a<1000**1000:
    l.append(a)
    a,b=b,a+b
while True:
    x=int(input("Enter a positive number/ negative number to exit the program: "))
    if x>=0:
        if x in l:
            print(x,"is valid")
        else:
            print(x,"is invalid")
    else:
        print("Wrong input. Negative numbers not supported!")
        exit()