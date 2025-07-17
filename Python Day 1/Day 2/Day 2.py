# Q: Assign your name and age to two variables and print them.
# Example output: My name is Ashutosh and I am 25 years old.
# S = "Sanket"
# Age = 26

# print(f"My name is {S} and I am {Age} years old.");

# Q: Identify which variable names are valid or invalid:
#_myvar = 'Sanket'
# my_var = 'Sanket'
# 2ndname = 'Sanket'   # invalid can't start with number
# user-name = 'Sanket' # invalid can't use - in variable
#class = 'Sanket'  # invalid can't use due to reserved keywords
# userName = 'Sanket'

# print(userName); 

# Try writing code with these names and see which give errors.
# Q: Assign values 10, 20, 30 to a, b, c in one line and print them.

# a, b, c = 10, 20 , 30

# print(a, b, c)


# Q: Assign the value 100 to variables x, y, z in one line. Then print all three.

# x = y = z = 100

# print(x, y, z)

# Q: Assign a float to a variable and print its type using type() function.

# number = 5.5
# print(number)
# print(type(number))

# Q: Take two variables a = 5, b = 10 and swap them without using a third variable.

# a = 5
# b = 10
# a, b = b,a # swaping values using tuple unpacking
# print("a = ", a)
# print("b = ", b)

# Q: Use f-string to print: "Ashutosh is 27 years old and lives in Pune"
# Use variables for name, age, city.

# name = "Sanket"
# age = 27
# city = "Mumbai"

# print(f"{name} is {age} years old and lives in {city}")

# Q: Take name and age as input from the user and print: "Hello, [name]! You are [age] years old."

# name = input ("Enter your name: ")
# age = input("Enter your age: ")

# print(f"Hello, {name}! You are {age} years old.")

# name = "Sanket"
# age = 26

# print(f"Hello, {name}! you are {age} years old")

# Q: Write a program to take 2 numbers from the user and print their sum, difference, product, and division.

# number1 = float(input("Enter the first number: "))
# number2 = float(input("Enter your second number: "))

# sum = number1 + number2
# difference = number1 - number2
# product = number1 * number2
# division = number1 / number2

# print(f"sum = {sum}")
# print(f"difference ={difference}")
# print(f"product = {product}")
# print(f"division ={division}")

# Q: Define a variable `PI = 3.14`. Use it to calculate the area of a circle with radius 5.
# Note: Though Python doesn't support constants, use capital letters as a convention.

# PI = 3.14
# radius = 5 

# area = radius * PI **2

# print(f"Area of the circle with Radius {radius} is Area {area} ")

# Q: Assign your first and last name to two variables.
# Print your full name in one line using string concatenation.

# firstname = "Sanket"
# lastname = "Salunke"

# fullname = firstname + " " + lastname

# print(f"Fullname =  {fullname}")

# Q: Create a variable with an underscore (e.g., user_age) and assign it a value.
# Print it using an f-string.

# full_name = "Sanket Salunke"

# print(f"Full Name of the User is {full_name}")


# Q: Create two variables `value` and `Value`, assign them different numbers.
# Print both and observe the output.

# value = 10
# Value =20
# # for case sensitive purpose
# print(value)
# print(Value)

# # Q: Assign an integer to variable `x`, then assign a string to the same `x`.
# # Print type before and after re-assignment.

# x = 10
# x = "sanket"

# print(x)

# Q: Try creating a variable named `class` and assign it a value.
# Observe the error and fix it with a valid name.

# class = 10 # invalid due to reserved keywords

# print(class)


# Q: Use `.format()` method to print: “The cost of 5 apples is ₹150”
# Use variables for quantity and price.

# qty = 10

# price = 200

# print("The cost of {} apple is rs {}".format(qty,price))


# Q: Print a message using `%s` and `%d` formatting style. Example: "User Ashutosh is 27 years old."

# name = "Sanket"
# age = 26

# # %s for string and %d for integer

# print("User %s is %d years old." % (name,age))

# Q: Assign values to multiple variables using line continuation:
# Example:
# x = 1 + \
#     2 + \
#     3
# Print x.

# x = 1 + \
#     2 + \
#     3

# print(x)

# Q: Assign the result of a mathematical expression (e.g., 10 + 5 * 2) to a variable.
# Print it.

# Total = 10 + 5 * 2

# print(Total)


# Q: x = y = z = 5 + 10
# Print x, y, z

# x = y = z = 5 + 10

# print(x, y, z)

# Q: Take two numbers as input from the user, assign to `a` and `b`, and print their average.

# A = float(input("Enter the first number"))
# B = float(input("Enter the second number"))

# Average = (A + B)/ 2

# print(f"Average vaule is {Average}")

# Q: Assign a string with special characters like newline (`\n`) and tab (`\t`) to a variable.
# Print it and observe the effect.

# ABC = "Hello \n Sanket \there"

# print(ABC)


# Q: Use `print(a, b, sep='-', end='!')` to customize print output.

# a = "Hello"
# b = "World"

# print(a, b, sep='-', end='!')  # not running


# Q: Create two variables with the same value and print their `id()` to check if they refer to the same object.

A =14
B =14

# print(A)
#  print(B)

print(f"value of A is {A} and value of B is {B}")

