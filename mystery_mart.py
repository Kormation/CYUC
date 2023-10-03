# Programmer :  Alexander Walker
# Description : This program generates a random price between 0-1000 and the user will pay with 100 dollar bills, then get change back equal to what is leftover.

#Import Functions
import random
import time
from math import ceil

#Variables, Determines item price, how much it cost in 100 dollar bills, and determines the change.
cash_value = random.uniform(0.00, 1000.00)
money = cash_value / 100
bills = ceil(money)
change = bills * 100 - cash_value

#Outputs the price, amount needed to pay, and their change
time.sleep(0.5)
print("Welcome to Mystery Mart")
time.sleep(2)
print (f"This product costs ${cash_value:,.2f}")
time.sleep(2)
print(f"Please pay {bills} hundred-dollar bills")
time.sleep(2)
print(f"Your change is ${change:,.2f}")
time.sleep(1)



    




