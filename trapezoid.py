# Programmer : Alexander Walker
# Description : This program will calculate the area of a trapezoid

import time

#Gets information on the trapezoid from the user and stores it
a = float(input("Enter the long base length: "))
time.sleep(0.2)
b = float(input("Enter the short base length: "))
time.sleep(0.2)
h = float(input("Enter the altitude: "))
time.sleep(0.5)

#Adds up the information and shows the user the are of their trapezoid
area = (a + b) / 2 * h
print(f"\nThe area is {area:,.1f}")

