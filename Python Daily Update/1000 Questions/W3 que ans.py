# # print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

#       -------------------------------------------------------

#  # Write a Python program to find out what version of Python you are using.


# import sys

# # Get the full version info
# version_info = sys.version_info

# # # Print the version
# print(f"You are using Python {version_info.major}.{version_info.minor}.{version_info.micro}")

# print(f"You are using Python {version_info}")

#       ---------------------------------------------------------------

# Write a Python program to display the current date and time.


# from datetime import datetime

# now = datetime.now()

# print("Current date and time:")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))


#       -------------------------------------------------------------------

#   # Write a Python program that calculates the area of a circle based on the radius entered by the user.

# import math

# radius = float(input("Enter the radius of the circle: "))

# area = math.pi * (radius ** 2)    # squares the radius (i.e.,r square)

# print(f"The area of the circle with radius {radius} is {area}")

#       -------------------------------------------------------------------


# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

# first_name = input("Enter your first name: ")

# last_name = input("Enter your last name: ")

# print(last_name + " " + first_name)

#       -----------------------------------------------------------------

# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

# # Get comma-separated numbers from the user
# input_str = input("Enter comma-separated numbers: ")

# # Split the string into a list using comma as the separator
# num_list = input_str.split(",")

# # Convert the list into a tuple
# num_tuple = tuple(num_list)

# # Display the results
# print("List:", num_list)
# print("Tuple:", num_tuple)


#           -----------------------------------------

# Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

# # Ask the user to enter a filename
# filename = input("Enter the filename: ")

# # Split the filename using '.' and get the last part
# # Handles filenames like "abc.java" → ['abc', 'java']
# # Handles "archive.tar.gz" → ['archive', 'tar', 'gz']
# extension = filename.split(".")[1]

# # Display the file extension
# print("The extension of the file is:", extension)


#           -------------------------------------------------

# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)

# exam_st_date = (11, 12, 2014)

# day, month, year = exam_st_date

# # Display the examination schedule
# print(f"Examination will start from: {day}/{month}/{year}")

#       --------------------------------------------------------------

# Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]

# color_list = ["Red", "Green", "White", "Black"]

# print("First color:", color_list[0])    # 0 means first initial value
# print("Last color:", color_list[-1])    # -1 means starts from last first value

#           --------------------------------------------------------------

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

# n = input("Enter an integer: ")

# result = int(n) + int(n**2) + int(n**3)   # Here int(n*2) means n repeats 2 times

# print("Result:", result)

#       --------------------------------------------------------------------------

# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.

# Program to print documentation of a Python built-in function

# print("Documentation for abs():")
# print("------------------------")
# help(abs)

#       ------------------------------------------


# Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module.

# import calendar

# year = int(input("Enter the year (like e.g 2025): "))
# month = int(input("Enter the month (like e.g - 1 to 12): "))  # Always give int as input data type


# print(calendar.month(year, month)) # to print year and month

#           -------------------------------------------------------------

# Write a Python program to print the following 'here document'.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

# To print multiline comment use triple  """Text""" for multiline string

# print("""a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example""")

#           -----------------------------------------------------------------

# Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

# from datetime import date

# date_1 = date(2025, 1, 10)
# date_2 = date(2025, 1, 1)

# Duration = date_1 - date_2

# print(f"{Duration.days} Days") 

#           ---------------------------

# Write a Python program to get the volume of a sphere with radius six.

# import math

# radius = 6 

# volume = (4/3) * math.pi * (radius ** 3)

# print(f"The volume of the sphere with radius{volume:.2f} ")

#           -----------------------------------------------------------------

# Write a Python program to calculate the difference between a given number and 17. 
# If the number is greater than 17, return twice the absolute difference.

# def difference_btwn_17(n):
#     if n > 17:
#         return 2 * abs(n - 17)  # multiply it by 2 to and return that value
#     else:
#         return abs(n - 17)
    
# num = int(input("Enter a Number: "))
    
# result = difference_btwn_17(num)

# print(f" The differencr btwn 17 and given number is{result}")

#           -----------------------------------------------------

# Write a Python program to test whether a number is within 100 of 1000 or 2000.

# def value(num):
#     return abs(1000 - num) <= 100 or abs(2000 - num) <= 100

# numbers=[1002, 300, 5000, 1950, 2300, 1500, 800, 2200]
# # numbers = [900, 950, 1100, 1900, 2100, 2200, 800]

# for number in numbers:
#     if value(number):
#         print(f"{number} is within 100 of 1000 or 2000.")
#     else:
#         print(f"{number} is NOT within 100 of 1000 or 2000.")

#           -----------------------------------------------------

# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

# def sum(a , b, c):
#     if a == b== c:
#         return 3 * (a + b + c)
#     else:
#         return (a + b + c)
    
# a = int(input("Enter yout first value: "))
# b = int(input("Enter yout second value: "))
# c = int(input("Enter yout third value: "))

# result = sum(a , b, c)

# print("Result: ",result)

#           -----------------------------------------------------------------

# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. 
# Return the string unchanged if the given string already begins with "Is".

# def add_is_prefix(s):
#     if s.startswith("Is"):  # startswith("Is"): checks input as "Is", if Is already there it will not be added
#         return s
#     else:
#         return "Is" + s  # If "Is" as input not there then Is + given input will be added 

# # Accept input from the user
# user_input = input("Enter a string: ")

# # Get the modified string
# result = add_is_prefix(user_input) # Here  If "Is" as input not there then Is + given input will be added 

# print("Result:", result)

#           --------------------------------------------------------------

# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

# def multiply_string(s, n):
#     if n < 0:
#         return "Error: n must be a non-negative integer."
#     return s * n

# string_input = input("Enter a string: ")
# n = int(input("Enter a non-negative integer: "))

# result = multiply_string(string_input,n)

# print("Result: ",result)

#       --------------------------------------------------------------

# Write a Python program that determines whether a given number (accepted from the user) is even or odd,
#  and prints an appropriate message to the user.

# num = int(input("Enter a number : "))

# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

#           -------------------------------------------------------------

# Write a Python program to count the number 4 in a given list.

# def count_fours(nums):
#     return nums.count(4)  # count(4) -> to count number given in (<->)

# numbers = [1,3,4,5,7,8,4,9]

# result = count_fours(numbers)

# print ("Number of 4 in the list: ", result)

#       -------------------------------------------------------------------

# Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string.
#  Return n copies of the whole string if the length is less than 2.

# def first_two_copies(s, n):
#     if n < 0:
#         return "Error: n must be a non-negative integer."
    
#     # Get the first two characters if string length >= 2
#     # Otherwise, use the whole string
#     part = s[:4] if len(s) >= 3 else s    # here you can declare s[1:5] if len(s) >= 3 else s string slicing with staring and ending point
#     return part * n

# text = input("Enter a string: ")
# num = int(input("Enter a non-negative integer: "))

# result = first_two_copies(text, num)  # here called those function values first_two_copies(text, num)

# print("Result:", result)

#           -----------------------------------------------------

# Write a Python program to test whether a passed letter is a vowel or not.

# letter = input("Enter a single letter: ").lower()

# if len(letter) == 1 and letter.isalpha:

#     if letter in 'aeiou':    # in 'aeiou' is to filter input values
#         print(f"{letter} id vowel.")
#     else:
#         print(f"{letter} is not vowel")
# else:
#     print("Please enter single alphabet letter only...")

#       -----------------------------------------------------

# Write a Python program that checks whether a specified value is contained within a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

# def value_in_group (value, group):
#     return value in group

# print ("3 -> [1, 5, 8, 3] :", value_in_group(3, [1, 5, 8, 3]))

# print ("-1 -> [1, 5, 8, 3]", value_in_group(-1, [1, 5, 8, 3]))

#       --------------------------------------------------------------

# Write a Python program to create a histogram from a given list of integers.

# def create_histogram (values):
#     for value in values:
#         print ('*' * value)  # * will be multipy with value

# number = [2,4,6,3,5]

# create_histogram(number) 

#       -------------------------------------------------------------

# Write a Python program that concatenates all elements in a list into a string and returns it.

# def concatenate_list_elements(lst):
#     return ''.join(str(element) for element in lst)

# my_list = ['Hello', ' ','Sanket', ' ','Salunke']

# result = concatenate_list_elements(my_list)

# print("concatenated stings", result)

#       --------------------------------------------------------------------

# Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence.
# Sample numbers list :

# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]

# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958, 743, 527]

# for num in numbers:
#     if num == 237:
#         break       # Stop the loop when 237 is found
#     if num % 2 == 0:
#         print(f"{num} is even")

#       -------------------------------------------------------

# Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

# color_list_1 = set(["White", "Black", "Red", "Yellow"])
# color_list_2 = set(["Red", "Green"])

# result = color_list_1 - color_list_2

# print("Colors in color_list_1 but not in color_list_2:")

# print(result)

#       ----------------------------------------------------------

# Write a Python program that will accept the base and height of a triangle and compute its area.

# base = float(input("Enter the base value: "))
# height = float(input("Enter the height value: "))

# area = 0.5 * base * height

# print(f"The area of the triangle is {area}")

#           -----------------------------------------------------------------------

# Write a Python program that computes the greatest common divisor (GCD) of two positive integers.

# import math

# a = int(input("Enter a first positive value: "))
# b = int(input("Enter a second positive value: "))

# gcd = math.gcd(a, b)

# print(f"The gcd of {a} and {b} is {gcd}")

# # 2 

# def compute_gcd(x, y):
#     while y != 0:
#         x, y = y, x % y
#     return x

# # Input
# a = int(input("Enter first positive integer: "))
# b = int(input("Enter second positive integer: "))

# # Output
# print("The GCD of", a, "and", b, "is:", compute_gcd(a, b))

#       --------------------------------------------------------------------

# Write a Python program to find the least common multiple (LCM) of two positive integers.

# import math

# a = int(input("Enter the first positive integer: "))
# b = int(input("Enter the second positive integer: "))

# if a > 0 and b > 0:
#     lcm = abs(a * b) // math.gcd(a, b)   # abs(a * b) takes positive value and return positive value // divide the  math.gcd(a, b) 

#     print(f"The LCM of {a} and {b} is {lcm}")
# else:
#     print("Please enter positive integers only.")

#       ---------------------------------------------------------------------------

# Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.

# def custom_sum(a, b, c):
#     if a == b or b == c or a == c:
#         return 0
#     return a + b + c

# x = int(input("Enter first integer: "))
# y = int(input("Enter second integer: "))
# z = int(input("Enter third integer: "))

# result = custom_sum(x, y, z)  
# print("Result:", result)

#           --------------------------------------------------------------------

# Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

# def custom_sum (a,b):
#     total = a + b
#     if 15 <= total < 20:
#         return 20
#     return total

# x = int(input("Enter first integer: "))
# y = int(input("Enter a second integer: "))

# result = custom_sum(x, y)

# print("Result: ", result)

#       ----------------------------------------------------------------------

# Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.

# def check_numbers(a, b):
#     return a == b or (a + b) == 5 or abs(a - b) == 5

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))

# print("Result:", check_numbers(x, y))

#       ------------------------------------------------------

# Write a Python program to add two objects if both objects are integers.

# def add_if_integers(a, b):
#     if isinstance(a, int) and isinstance(b, int):
#         return a + b
#     else:
#         return "Both inputs must be integers."

# x = input("Enter first value: ")
# y = input("Enter second value: ")

# try:
#     x = int(x)
#     y = int(y)
# except ValueError:
#     print("Error: Inputs must be integers.")
# else:

#     result = add_if_integers(x, y)
#     print("Result:", result)

#           ------------------------------------------------------

# Write a Python program that displays your name, age, and address on three different lines.

# name = "Sanket Salunke"
# age = 26
# address = "Ekta apartment Airoli sectoe 17 Airoli..."

# print("Name:", name)
# print("Age:", age)
# print("Address:", address)

# print(f"""{name} \n Ekta apartment \n Airoli sector 17, \n {age} Airoli {address}""")

#       ----------------------------------------------------------------------

# Write a Python program to solve (x + y) * (x + y).
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49

# x = 4
# y = 3

# result = (x + y) * (x + y)

# print(f"{x} + {y} ^ 2 = {result}")

#       -------------------------------------------------------------

# Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

# amt = 10000
# rate = 3.5 
# years = 7

# future_value = amt * (1 + rate / 100) ** years

# print("Future Value:", round(future_value, 2))

#           ---------------------------------------------------------------

# Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).

# import math

# x1 = float(input("Enter x1: "))
# y1 = float(input("Enter y1: "))
# x2 = float(input("Enter x2: "))
# y2 = float(input("Enter y2: "))

# distance = math.sqrt((x2 - x1)**2-(y2 - y1)**2)

# print(f"The distance between the points {x1}, {y1} and {x2}, {y2} is {distance:.2f} ")

#       ----------------------------------------------------------------------

# Write a Python program to check whether a file exists.

# from pathlib import Path 

# file_path = input ("Enter the file path: ")

# path = Path(file_path)

# # Check existence
# if path.exists():
#     print("File exists.")
# else:
#     print("File does not exist.")

#  2 ----

# import os

# file_path = input ("Enter the file path: ")

# if os.path.exists(file_path):
#     print("File exists: ")

# else:
#     print("File does not exist.")

#       ------------------------------------------------------

# Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

# import platform

# # Get architecture info
# arch = platform.architecture()[0]

# # Display result
# print(f"Python is running in {arch} mode.")

# #   #  #  ---------------------
# import struct

# # Determine bit mode based on pointer size
# bits = struct.calcsize("P") * 8

# print(f"Python is running in {bits}-bit mode.")

#          -----------------------------------------------------

# Write a Python program to get OS name, platform and release information.

# import os 
# import platform

# os_name = os.name

# system = platform.system()
# release = platform.release()

# print("Os name: ", os_name)
# print("Platform system: ", system)
# print("Platform release: ", release)

#       -----------------------------------------------------

# Write a Python program to locate Python site packages.

# import site

# # Get list of site-packages directories
# site_packages = site.getsitepackages()

# # Display each path
# print("Python site-packages directories:")
# for path in site_packages:
#     print(path)

#           -----------------------------------------------

# Write a Python program that calls an external command.

# import subprocess

# # Run an external command (example: echo)
# result = subprocess.run(["echo", "Hello from the shell!"], capture_output=True, text=True)

# # Print the output
# print("Command output:", result.stdout.strip())

# import subprocess

# # For Windows:
# # subprocess.run(["dir"], shell=True)

# # For Unix/Linux/macOS:
# subprocess.run(["ls", "-l"])

#  # not running 

#           --------------------------------


# Write a Python program to retrieve the path and name of the file currently being executed.

# import os

# # Get the full path of the currently executing file
# file_path = os.path.abspath(__file__)

# # # file_path = os.path.abspath("Git-Python") 

# # Display the result
# print("Full path of the currently executing file:")
# print(file_path)

#           --------------------------------------------------


# Write a Python program to find out the number of CPUs used.

# import multiprocessing

# # Get the number of CPUs
# cpu_count = multiprocessing.cpu_count()

# print(f"Number of CPUs available: {cpu_count}")

#           -------------------------------------------------------------

# Write a Python program to parse a string to float or integer.

# def parse_number(s):
#     try:
#         # Try to convert to integer first
#         result = int(s)
#         print(f"Parsed as integer: {result}")
#     except ValueError:
#         try:
#             # Try to convert to float if int fails
#             result = float(s)
#             print(f"Parsed as float: {result}")
#         except ValueError:
#             print("Input is not a valid number.")

# # Example usage
# user_input = input("Enter a number: ")
# parse_number(user_input)


#       ----------------------------------------------------