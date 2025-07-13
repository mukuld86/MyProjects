"""n=input("Enter a character:")
s="abcdefghijklmnopqrstuvwxyz"
S=s.upper()
string=s+S
i=0
X=string[i]
while(i<53):
    if(n in string):
        N=int(input("Enter a digit:"))
        if(N!=9):
            print("wrong input")
        else:
            break
    else:
            break
    i+=1
"""
ch = input()[:1]
if ch.isalpha():
    n = input("Enter a digit: ")
    if int(n) != 9:
        print("wrong input")
