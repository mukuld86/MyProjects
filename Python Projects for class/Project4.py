import random
S="abcdefghijklmnopqrstuvwxyz1234567890@#_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l=int(input("Enter required length of password: "))
passw=""
for i in range(1,l+1):
    passw+=random.choice(S)
print(passw)