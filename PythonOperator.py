
#OPERATORS IN PYTHON

#Assignment Operators
#Assignment operators are used to assign values to variables.
	# x = 5	x = 5	
	# x += 3	x = x + 3	
	# x -= 3	x = x - 3	
	# x *= 3	x = x * 3	
	# x /= 3	x = x / 3	
	# x %= 3	x = x % 3	
	# x //= 3	x = x // 3	
	# x **= 3	x = x ** 3	
	# x &= 3	x = x & 3	
	# x |= 3	x = x | 3	
	# x ^= 3	x = x ^ 3	
	# x >>= 3	x = x >> 3	
	# x <<= 3	x = x << 3

# Arithmetic Operators:
# Addition(+): a + b
# Subtraction(-): a - b
# Multiplication(*): a * b
# Division(/): a / b
# Modulus(%): a % b
# Floor division(//): a // b
# Exponentiation(**): a ** b
# Declaring values and organizing them together
from importlib.metadata import packages_distributions


num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

#Comparison Operators
# we use comparison operators to compare two values.
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

# We check if a value is greater or less or equal to other value.
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

#Logical Operators
# python uses keywords and, or and not for logical operators. 
# Logical operators are used to combine conditional statements
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False


#EXERCISE
# Write a script that prompts the user to enter base and height of the triangle and
# calculate an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100

b = int(input("Enter base: "))
h = int(input("Enter height: "))
area_of_traingle = 0.5 * b * h
print(area_of_traingle)


# Write a script that prompts the user to enter side a, side b, and side c of the triangle.
# Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side b: "))
perimeter_of_traingle = a + b + c
print(perimeter_of_traingle)


# Get length and width of a rectangle using prompt. 
#Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
l = int(input("Enter lenght: "))
w = int(input("Enter width: "))
area_of_rec = l * w
print(area_of_rec)

perimeter_of_rec = 2 * (l + w)
print(perimeter_of_rec)


# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and
# circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
rad = int(input("Enter radius: "))
area_of_circle = pi * rad * rad
print(area_of_circle)

circum_of_circle = 2 * pi * rad
print(circum_of_circle)


# Calculate the slope, x-intercept and y-intercept of y = 2x -2

# Slope is (m = y2-y1/x2-x1). Find the slope and
# Euclidean distance between point (2, 2) and point (6,10)
# Compare the slopes in tasks 8 and 9.

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and 
# figure out at what x value y is going to be 0.


# Even numbers are divisible by 2 and the remainder is zero.
# How do you check if a number is even or not using python?

# Check if the floor division of 7 by 3 is equal to the 
# int converted value of 2.7.

# Check if type of '10' is equal to type of 10
print((type('10'))==(type(10)))

# Check if int('9.8') is equal to 10
print((int('9.8'))==(10))


# Writ a script that prompts the user to enter hours and rate per hour. 
# Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.
# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125