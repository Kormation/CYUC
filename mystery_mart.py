# Programmer :  Alexander Walker
# Description : This program generates a random price between 0-1000 and the user will pay with
# A certain amount of bills, then get change back equal to what is left.

#Import Functions
import random
import time
from math import ceil

#Giving cash value a random number between 0.00 - 1000.00
cash_value = random.uniform(0.00, 1000.00)



# If cash_value great then 0 but less the 100 then...
if (cash_value == 0):
    change = 0 
    time.sleep(0.5)
    print("Welcome to Mystery Mart")
    time.sleep(2)
    print (f"This product costs ${cash_value:,.2f}")
    time.sleep(2)
    print("Please pay 0 hundred-dollar bills")
    time.sleep(2)
    print(f"Your change is ${change:,.2f}")
    time.sleep(1)

# If cash_value great then 0 but less the 100 then...
if (cash_value > 0) and (cash_value <= 100):
    change = 100 - cash_value
    time.sleep(0.5)
    print("Welcome to Mystery Mart")
    time.sleep(2)
    print (f"This product costs ${cash_value:,.2f}")
    time.sleep(2)
    print("Please pay 1 hundred-dollar bills")
    time.sleep(2)
    print(f"Your change is ${change:,.2f}")
    time.sleep(1)
    
# If cash_value great then 100 but less the 200 then...   
elif (cash_value > 100) and (cash_value <= 200):
    change = 200 - cash_value
    time.sleep(0.5)
    print("Welcome to Mystery Mart")
    time.sleep(2)
    print (f"This product costs ${cash_value:,.2f}")
    time.sleep(2)
    print("Please pay 2 hundred-dollar bills")
    time.sleep(2)
    print(f"Your change is ${change:,.2f}")
    time.sleep(1)
    
# If cash_value great then 200 but less the 300 then...
elif (cash_value > 200) and (cash_value <= 300):
    change = 300 - cash_value
    time.sleep(0.5)
    print("Welcome to Mystery Mart")
    time.sleep(2)
    print (f"This product costs ${cash_value:,.2f}")
    time.sleep(2)
    print("Please pay 3 hundred-dollar bills")
    time.sleep(2)
    print(f"Your change is ${change:,.2f}")
    time.sleep(1)

# If cash_value great then 300 but less the 400 then...
elif (cash_value > 300) and (cash_value <= 400):
    change = 400 - cash_value
    time.sleep(0.5)
    print("Welcome to Mystery Mart")
    time.sleep(2)
    print (f"This product costs ${cash_value:,.2f}")
    time.sleep(2)
    print("Please pay 4 hundred-dollar bills")
    time.sleep(2)
    print(f"Your change is ${change:,.2f}")
    time.sleep(1)
    
# If cash_value great then 400 but less the 500 then...
elif (cash_value > 400) and (cash_value <= 500):
    change = 500 - cash_value
    time.sleep(0.5)
    print("Welcome to Mystery Mart")
    time.sleep(2)
    print (f"This product costs ${cash_value:,.2f}")
    time.sleep(2)
    print("Please pay 5 hundred-dollar bills")
    time.sleep(2)
    print(f"Your change is ${change:,.2f}")
    time.sleep(1)
    
# If cash_value great then 500 but less the 600 then...
elif (cash_value > 500) and (cash_value <= 600):
    change = 600 - cash_value
    time.sleep(0.5)
    print("Welcome to Mystery Mart")
    time.sleep(2)
    print (f"This product costs ${cash_value:,.2f}")
    time.sleep(2)
    print("Please pay 6 hundred-dollar bills")
    time.sleep(2)
    print(f"Your change is ${change:,.2f}")
    time.sleep(1)
    
# If cash_value great then 600 but less the 700 then...
elif (cash_value > 600) and (cash_value <= 700):
    change = 700 - cash_value
    time.sleep(0.5)
    print("Welcome to Mystery Mart")
    time.sleep(2)
    print (f"This product costs ${cash_value:,.2f}")
    time.sleep(2)
    print("Please pay 7 hundred-dollar bills")
    time.sleep(2)
    print(f"Your change is ${change:,.2f}")
    time.sleep(1)
    
# If cash_value great then 700 but less the 800 then...
elif (cash_value > 700) and (cash_value <= 800):
    change = 800 - cash_value
    time.sleep(0.5)
    print("Welcome to Mystery Mart")
    time.sleep(2)
    print (f"This product costs ${cash_value:,.2f}")
    time.sleep(2)
    print("Please pay 8 hundred-dollar bills")
    time.sleep(2)
    print(f"Your change is ${change:,.2f}")
    time.sleep(1)
    
# If cash_value great then 500 but less the 600 then...
elif (cash_value > 800) and (cash_value <= 900):
    change = 900 - cash_value
    time.sleep(0.5)
    print("Welcome to Mystery Mart")
    time.sleep(2)
    print (f"This product costs ${cash_value:,.2f}")
    time.sleep(2)
    print("Please pay 9 hundred-dollar bills")
    time.sleep(2)
    print(f"Your change is ${change:,.2f}")
    time.sleep(1)
    
# If cash_value great then 900 but less the 1000 then...
elif (cash_value > 900) and (cash_value <= 1000):
    change = 1000 - cash_value
    time.sleep(0.5)
    print("Welcome to Mystery Mart")
    time.sleep(2)
    print (f"This product costs ${cash_value:,.2f}")
    time.sleep(2)
    print("Please pay 10 hundred-dollar bills")
    time.sleep(2)
    print(f"Your change is ${change:,.2f}")
    time.sleep(1)


    




