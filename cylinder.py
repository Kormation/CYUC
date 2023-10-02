# Programmer : Alexander Walker
# Description : This program calculates the area and volume of a cylinder

# Imports the math function so we can use pi / π
import math
from math import pi, sqrt

# User puts in the diameter and height of a cylinder
diameter = float(input("Enter the diameter: "))
height = float(input("Enter the height: "))

# Stores diameter, and height in a smaller veriable
r = diameter / 2
h = height

# Calculates the volue, and surface area of the cylinder.
volume = pi * (r ** 2) * h
surface_area = (2 * pi * r ** 2) + (2 * pi * r * h)

# Shows the user the answer
print(f"\nThe volume is {volume:,.3f}")
print(f"The surface area is {surface_area:,.3f}")

