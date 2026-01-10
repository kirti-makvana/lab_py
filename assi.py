# 1 Print Message
print("hello world")

# 2 Add to Number
# Get two numbers from user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculate and print the sum
total = num1 + num2
print(f"The sum of {num1} and {num2} is {total}")

# 3. even or odd
num = int(input("Enter a number: "))
if num & 1:
    print(f"{num} is Odd")
else:
    print(f"{num} is Even")

# 4 leap yr    
# Get year from user input
year = int(input("Enter a year: "))

# Check leap year conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# 5 PI(3.14)
import math

# Print pi value
print(math.pi)

# 6 store and print constant value
# Define constants (ALL_CAPS convention)
PI = 3.14159
SPEED_OF_LIGHT = 299792458  # m/s

# Print constants
print(f"PI: {PI}")
print(f"Speed of light: {SPEED_OF_LIGHT} m/s")

def square_number(num):
    return num ** 2

# 7 square of a number
num = float(input("Enter a number: "))
print(f"Square: {square_number(num)}")

#8 area of circle

import math

# Get radius from user input
radius = float(input("Enter the radius: "))

# Calculate area
area = math.pi * radius ** 2

print(f"Area of circle with radius {radius}: {area:.2f}")


# 9 check data type
# User input and type checking
value = input("Enter a value: ")

print(f"Type: {type(value)}")  # Shows <class 'str'>

# Common type checks
num = 42
print(f"42 is int: {isinstance(num, int)}")  # True
print(f"42 is float: {isinstance(num, float)}")  # False

# 10 use math functions
import math

# User input
num = float(input("Enter a number: "))

# Basic math functions
print(f"Square root: {math.sqrt(num):.2f}")
print(f"Power (num^2): {math.pow(num, 2):.2f}")
print(f"Ceiling: {math.ceil(num)}")
print(f"Floor: {math.floor(num)}")
print(f"Absolute: {math.fabs(num)}")

# 11 find power
# Get base and exponent from user
base = float(input("Enter base number: "))
exponent = float(input("Enter exponent: "))

# Calculate power
result = base ** exponent
print(f"{base}^{exponent} = {result}")

# 12 check positive or negative
# Get number from user input
num = float(input("Enter a number: "))

# Check positive, negative, or zero
if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
else:
    print(f"{num} is Zero")
