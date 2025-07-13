# write a program to print the table of a number x taken as input from the user up to a number y also taken as input
# Maximum number of rows that that can be taken is 20

x = int(input())
y = int(input())
if y > 20:
    for i in range(1, 21):
        print("{} * {} = {}".format(x, i, x * i))
    else:
        print("rows limited is 20")
else:
    for i in range(1, y + 1):
        print("{} * {} = {}".format(x, i, x * i))
