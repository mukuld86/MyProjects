"""
Compute the volume of a cylinder
Write a Program that reads in the radius and length of a cylinder and compute the area and volume.
Use the following formulas:
area = radius * radius * 3.14
volume = area * length

Sample run of the program:
Enter the radius and length of a cylinder:5.5,12
The area is 95.0331
The volume is 1140.4

"""
radius = float(input("Enter the radius"))
length = float(input("Enter the length"))
area = radius * radius * 3.14
volume = area * length
print("The area is", area)
print("The volume is", volume)
