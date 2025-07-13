"""write a program to calculate the electricity bill, we must understand electricity charges and rates:
 1-100 unit=1.5/-
 101-200 unit=2.5/-
 201-300 unit=4/-
 300-350 unit=5/-
 above 350- 15/-
 """
U = float(input("Enter units: "))
r = 0
if 1 <= U <= 100:
    r = 1.5
elif 100 < U <= 200:
    r = 2.5
elif 200 < U <= 300:
    r = 4
elif 300 < U <= 350:
    r = 5
else:
    r = 15

print("The Electricity Bill is worth", U * r, "Rs.")
