"""
Write a program that prompts the user to enter a weight in pound and height in inches and then displays the BMI.
Note that one pound is 0.45359237 kilograms and one inch is 0.0254 meters. Use laddered ifs statement.

bmi=weighInKilograms/(heightInMeter*heightInMeters)
"""
# w=150
# h=70

w = float(input("Enter weight in pounds:"))
h = float(input("Enter height in inches:"))
W = w * 0.45359237      # weight converted in Kgs
H = h * 0.0254          # height converted in meters
bmi = W / (H * H)
print("BMI is", bmi)

if bmi < 18.5:
    print("Underweight")
if bmi < 25:
    print("Normal")
if bmi > 30:
    print("Overweight")
else:
    print("Obese")
