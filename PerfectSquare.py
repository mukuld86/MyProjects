# Write a program check if the entered number is a perfect square or not
a = int(input("Enter a positive number: "))
if a ** (1/2) == int(a**(1/2)):
    print("Number is a perfect square")
else:
    print("Number is not a perfect square")
