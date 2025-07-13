"""
Suppose you shop for rice and find it in two different sized packages.
You would like to compare the costs of the packages.
the program prompts the user to

"""
w1 = int(input("Enter wight for Package1:"))
p1 = int(input("Enter price for Package1"))
w2 = int(input("Enter wight for Package2:"))
p2 = int(input("Enter price for Package2"))
r1 = p1 * w1
r2 = p2 * w2
if r1 < r2:
    print("Package 1 has better price")
elif r2 < r1:
    print("Package 2 has better price")
else:
    print("Both packages have same price")
