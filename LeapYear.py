# write a program to check if the entered year is a leap year or not
y = int(input("Enter a Year: "))
if y % 4 == 0 and y % 100 != 0:
    print("Entered year is a leap year")
elif y % 100 == 0 and y % 400 == 0:
    print("Entered Year is a leap Year")
else:
    print("Entered Year is not a leap Year")
