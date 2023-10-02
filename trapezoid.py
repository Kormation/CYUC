# Programmer : Alexander Walker
# Description : This program will calculate the area of a trapezoid

#Gets information on the trapezoid from the user and stores it
a = float(input("Enter the long base length: "))
b = float(input("Enter the short base length: "))
h = float(input("Enter the altitude: "))

#Adds up the information and shows the user the are of their trapezoid
area = (a + b) / 2 * h
print()
print(f"The area is {area:,.1f}")

