# Programmer : Alexander Walker
# Description : Get three integers from the user.  Find their average, maximum and minimum.


# Get three integers from the user
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter an integer: "))
num3 = int(input("Enter an integer: "))

# Calculate the average of the integers
average = (num1 + num2 + num3) / 3

# Find the biggest and smallest numbers
biggest = max(num1, num2, num3)
smallest = min(num1, num2, num3)

# Print the results
print()
print(f"The total is {average}")
print(f"The biggest integer is {biggest}")
print(f"The smallest integer is {smallest}")