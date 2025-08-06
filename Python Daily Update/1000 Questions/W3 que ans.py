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

# Write a Python program to list all files in a directory.

#   -----------------------------------------------------------

# Write a Python program to print without a newline or space.

# # end='' disables that so the next print() continues on the same line with no space

# print('s', end='')
# print('a', end='')
# print('n', end='')
# print('k', end='')
# print('e', end='')
# print('t', end='')

#       ----------------------------------------------------------------------

# Write a Python program to determine the profiling of Python programs.
# Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. 
# These statistics can be formatted into reports via the pstats module.


# import cProfile
# import pstats

# # A sample function to profile
# def slow_function():
#     total = 0
#     for i in range(1, 10000):
#         for j in range(i):
#             total += (i + j)
#     return total

# # Profile the function and print stats
# def run_profile():
#     profiler = cProfile.Profile()
#     profiler.enable()
#     slow_function()
#     profiler.disable()

#     # Create a Stats object and print sorted stats
#     stats = pstats.Stats(profiler)
#     stats.strip_dirs()               # Clean up file paths
#     stats.sort_stats('cumtime')      # Sort by cumulative time
#     stats.print_stats(10)            # Print top 10 functions

# # Run the profiler
# run_profile()

# #       -----------------------------------------------------------------------------

# Write a Python program to print to STDERR.

# import sys

# print("This is an error message.", file=sys.stderr)

# #         ------------------------------------------------------------

# import os

# # Access a specific environment variable (e.g., 'HOME' or 'PATH')
# home = os.environ.get('HOME')   # On Unix/Linux/Mac
# # home = os.environ.get('USERPROFILE')  # Use this on Windows

# path = os.environ.get('PATH')

# print("HOME directory:", home)
# print("PATH variable:", path)

# # List all environment variables
# print("\nAll environment variables:")
# for key, value in os.environ.items():
#     print(f"{key}: {value}")

# 55 to 57
# #         ----------------------------------------------------------------------

# Write a Python program to sum the first n positive integers.


# n = int(input("Enter a positive integer: "))

# if n <= 0:
#     print("Please enter a positive integer.")

# else:
#     total = n * (n + 1) // 2
#     print(f"The sum of the first {n} positive integers is: {total}")

#      ------------------------------------------------------------------

# Write a Python program to convert height (in feet and inches) to centimeters.

# inch_to_cm = 2.54
# feet_to_inches = 12

# feet = int(input("Enter height in feet: "))
# inches = int(input("Enter additional inches: "))

# total_inches = (feet * feet_to_inches) + inches

# height_cm = total_inches * inch_to_cm

# print(f"Height in centimeters {height_cm:.2f}cm ")
# print(f"Total inches of feet{feet} to inches is {total_inches}")

#    #  --------------------------------------------------------------------

# Write a Python program to calculate the hypotenuse of a right angled triangle.

# import math

# a = float(input("Enter the length of side a: "))
# b = float(input("Enter the length of side b: "))

# hypotenuse = math.sqrt(a**2 + b**2)

# print(f"The hypotenuse of the triangle is {hypotenuse:.2f} ")


#       ---------------------------------------------------------------

# Write a Python program to convert the distance (in feet) to inches, yards, and miles.

# feet = float(input("Enter distance in feet: "))

# inches = feet * 12
# yards = feet / 3
# miles = feet / 5280

# print(f"\n Distance conversion for {feet}feet")
# print(f"Inches: {inches}")
# # # print(f"Yards: {yards:.2f}")
# # # print(f"Miles: {miles:.2f}")

# print(f"Yards: {yards}")
# print(f"Miles: {miles}")

#               ----------------------------------------------------------------------

# Write a Python program to convert all units of time into seconds.

# days = int(input("Enter number of days: "))
# hours = int(input("Enter number of hours: "))
# minutes = int(input("Enter number of minutes: "))
# seconds = int(input("Enter number of seconds: "))

# total_seconds = (
#     days * 24 * 60 * 60 +
#     hours * 60 * 60 +
#     minutes * 60 +
#     seconds 
# )

# print(f"Total time in seconds: {total_seconds}")

#       #-  # 64-----------------------------------------

# Write a Python program to calculate the body mass index.

# weight = float(input("Enter your weight in Kilogram: "))
# height = float(input("Enter your height in meters: "))

# bmi = weight / (height ** 2)

# print(f"Your body mass index is {bmi:.2f}")

# if bmi < 18.5:
#     category = "Underweight"
# elif 18.5 <= bmi < 25:
#     category = "Normal weight"
# elif 25 <= bmi < 30:
#     category = "Over Weight"
# else:
#     category = "obese"

# print(f"BMI category: {category}")

#       ------------------------------------------

#Write a Python program to convert pressure in kilopascals to pounds per square inch, 
# a millimeter of mercury (mmHg) and atmosphere pressure.

# kpa = float(input("Enter pressure in kilopascals (kPa): "))

# psi = kpa * 0.145038
# mmhg = kpa * 7.50062
# atm = kpa / 101.325

# print(f"\nPressure conversions for {kpa} kPa:")
# print(f"Pounds per square inch (psi): {psi:.2f}")
# print(f"Millimeters of mercury (mmHg): {mmhg:.2f}")
# print(f"Atmospheres (atm): {atm:.3f}")

#       ------------------------------------------------------------------

# Write a Python program to calculate sum of digits of a number.


# num = input("Enter a number: ")

# digit_sum = 0

# for digit in num:
#     if digit.isdigit():  # Make sure it's a digit (ignores minus sign, dots, etc.)
#         digit_sum = digit_sum + int(digit)

# print(f"Sum of digits: {digit_sum}")

#       --------------------------------------------------------------------

# Write a Python program to sort three integers without using conditional statements and loops.

# a = int(input("Enter first integer: "))
# b = int(input("Enter second integer: "))
# c = int(input("Enter third integer: "))

# sorted_values = sorted([a, b, c])

# print("Sorted integers:", sorted_values)


#       -----------------------------------------------------

#  # # 70 71 #  ----------------------------------------

# Write a Python program to get the details of the math module.

# import math

# # List all functions, constants, etc. in the math module
# print("List of available functions and constants in math module:\n")
# print(dir(math))  # # to get all list 

# # OR use help() for detailed documentation
# print("\nDetailed help on math module:\n")
# help(math)   # # # Documetation and description of functions 

#       ------------------------------------------------------------------------------------


# Write a Python program to calculate the midpoints of a line.

# x1 = float(input("Enter x-coordinate of the first point: "))
# y1 = float(input("Enter y-coordinate of the first point: "))
# x2 = float(input("Enter x-coordinate of the second point: "))
# y2 = float(input("Enter y-coordinate of the second point: "))

# mid_x = (x1 + x2) / 2
# mid_y = (y1 + y2) / 2

# print(f"The midpoint of the line is: ({mid_x}, {mid_y})")

#          -------------------------------------------------------------

# Write a Python program to hash a word.

# import hashlib

# word = input("Enter a word to hash: ")

# hashed_word = hashlib.sha256(word.encode()).hexdigest()

# print(f"SHA-256 hash of '{word}':\n{hashed_word}")


#       ----------------------------------------------------------

# Write a Python program to get the copyright information and write Copyright information in Python code.

# import sys

# print("Python Copyright Information:")
# print(sys.copyright)

#           --------------------------------------------------------------------

# #  76 77

# Write a Python program to get the size of an object in bytes.

# import sys

# # Example objects
# x = 42
# y = "Hello, world!"
# z = [1, 2, 3, 4, 5]

# # Get and print sizes
# print(f"Size of integer x: {sys.getsizeof(x)} bytes")  #  getsizeof(x) -------> to get size of an object call through import sys
# print(f"Size of string y: {sys.getsizeof(y)} bytes")
# print(f"Size of list z: {sys.getsizeof(z)} bytes")

#       -----------------------------------------------------

# Write a Python program to get the current value of the recursion limit.

# import sys

# current_list = sys.getrecursionlimit()

# print(f"Current recurssion limit: {current_list}")

#       --------------------------------------------------------------

# Write a Python program to concatenate N strings.

# n = int(input("Enter the number of strings to concatenate: "))

# strings = []

# for i in range(n):
#     s = input(f"Enter string {i + 1}: ")
#     strings.append(s)

# result = ''.join(strings)

# print("Concatenated string:", result)

#       -----------------------------------------------------------------

# Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary).

# def sum_container(container):
#     if isinstance (container, dict):
#         return sum (container.values())
#     elif isinstance(container, (list,tuple,set)):
#         return sum (container)
#     else:
#         return "Unsupported data type"
    
# example_list = [1, 2, 3, 4]
# example_tuple = (10, 20, 30)
# example_set = {5, 10, 15}
# example_dict = {'a': 100, 'b': 200, 'c': 300}

# print("Sum of list:", sum_container(example_list))
# print("Sum of tuple:", sum_container(example_tuple))
# print("Sum of set:", sum_container(example_set))
# print("Sum of dictionary values:", sum_container(example_dict))

#       ------------------------------------------------------------

# Write a Python program to test whether all numbers in a list are greater than a certain number.

# numbers = [10, 20, 35, 50, 60, 70, 80]

# threshold = int(input("Enter the number to compare against: "))

# if all(num > threshold for num in numbers):    # all() checks if every element in the list satisfies the condition
#     print(f"All numbers in the list are greater than {threshold}.")
# else:
#     print(f"Not all numbers are greater than {threshold}.")


#       --------------------------------------------------------------

# Write a Python program to count the number of occurrences of a specific character in a string.

# text = input("Enter a string: ")
# char = input("Enter the character to count: ")

# # Check that only one character was entered
# if len(char) != 1:
#     print("Please enter a single character.")
# else:
#     count = text.count(char)
#     print(f"The character '{char}' appears {count} time(s) in the string.")

#       ---------------------------------------------------------------------------------

#  # 85     --------------------------------------------------------------------

# Write a Python program to get the ASCII value of a character.

# char = input("Enter a character: ")

# if len(char) != 1:
#     print("Please enter exactly one character.")
# else:
#     ascii_value = ord(char)
#     print(f"The ASCII value of '{char}' is: {ascii_value}")

#       -------------------------------------------------------------

# #  87

#       -------------------

# Given variables x=30 and y=20, write a Python program to print "30+20=50".

# x = 30
# y = 20

# print(f"{x}+{y}={x + y}")


#       ----------------------------------------------------------

#  # 89

#           ----------------------------------

# Write a Python program to perform an action if a condition is true.
# Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.


# day = int(input("Enter the day of the month: "))

# if day == 1:
#     print("First day of a Month!")

#       ---------------------------------------------------

# Write a Python program to swap two variables.

# a = input("Enter value for a: ")
# b = input("Enter value for b: ")

# print(f"\nBefore swapping: a = {a}, b = {b}")

# a, b = b, a

# print(f"After swapping: a = {a}, b = {b}")

#           ---------------------------------------------------------

# Write a Python program to define a string containing special characters in various forms.

# # Using escape sequences
# escaped_str = "Line1\nLine2\tTabbed\\Backslash\'Quote\"DoubleQuote"

# # Using Unicode characters (e.g., smiley face and heart)
# unicode_str = "Unicode examples: \u263A \u2665"

# # Using a raw string (ignores escape sequences)
# raw_str = r"This is a raw string:\n\t\\Nothing will be escaped"

# # Print all strings
# print("Escaped string:")
# print(escaped_str)

# print("\nUnicode string:")
# print(unicode_str)

# print("\nRaw string:")
# print(raw_str)

#           ----------------------------------------------------------------

# Write a Python program to get the Identity, Type, and Value of an object.

# obj = input("Enter something: ")

# # Identity (memory address), Type, and Value
# print("Identity (id):", id(obj))
# print("Type:", type(obj))
# print("Value:", obj)

#               ---------------------------------------------------------------

# Write a Python program to convert the bytes in a given string to a list of integers.

# # Input string from user
# text = input("Enter a string: ")

# # Convert the string to bytes (UTF-8) and then to a list of integers
# byte_list = list(text.encode('utf-8'))

# # Display the result
# print(f"Bytes as integers: {byte_list}")

#       --------------------------------------------------

# Write a Python program to check whether a string is numeric.


# # Get input from the user
# s = input("Enter a string: ")

# if s.isnumeric():
#     print("The string is numeric.")
# else:
#     print("The string is not numeric.")

#           ------------------------------------------------------------

#   #  96 97

#       ----------------------------------------

# Write a Python program to get system time.

# Note : The system time is important for debugging, network information, random number seeds,
#  or something as simple as program performance.

# from datetime import datetime

# current_time = datetime.now().time()

# print(current_time)

# ## 2 nd 

# import time

# current_time = time.strftime("%H:%M:%S")

# print("Current System Time:", current_time)

#           ----------------------------------------------

#  # 99

# Write a Python program to get the name of the host on which the routine is running.

# import socket

# host_name = socket.gethostname()

# print(host_name)

#              -----------------------------------------------------------------------------

# Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.


# numbers = [15, 30, 22, 45, 60, 17, 19, 90, 100, 105]

# divisible_by_15 = list(filter(lambda x: x % 15 == 0, numbers))

# print("Numbers divisible by 15:", divisible_by_15)

#                        -----------------------------------------------------------------

# Write a Python program to remove the first item from a specified list.

# my_list = [10, 20, 30, 40, 50, 60, 70]

# if my_list:
#     removed_item = my_list.pop(2)   # # pop(0) '0' defines position to removes and returns the element.
#     print(f"Removed item: {removed_item}")
# else:
#     print("The list id empty")

# print(f"Updated List: {my_list}")

#           ----------------------------------------------------------------------

# Write a Python program that inputs a number and generates an error message if it is not a number.

# user_input = input("Enter a number: ")

# try:
#     number = float(user_input)
#     print(f"You entered a number: {number}")
# except ValueError:
#     print("Error, this is not a valid number")

#           ----------------------------------------------------------------

# Write a Python program to filter positive numbers from a list.

# numbers = [14,-5,-10, 0, 5, -3, 8, 12, -7]

# positive_numbers = list(filter(lambda x: x > 0, numbers)) # #  lambda x: x > 0, gives positive value

# print(positive_numbers)

#       -------------------------------------------------------------------


# Write a Python program to compute the product of a list of integers (without using a for loop).

# from functools import reduce

# numbers = [2, 3, 4, 5]

# if numbers:
#     product = reduce(lambda x, y: x * y, numbers)
#     print("Product:", product)
# else:
#     print("The list is empty.")

#       -------------------------------------------------------------------


# Write a Python program to print Unicode characters.

# # Using escape sequences
# print("Unicode smiley face (\\u263A):", "\u263A")  # ☺
# print("Unicode heart (\\u2665):", "\u2665")        # ♥

# # Using chr() and code points
# print("Greek capital letter Omega (code point 937):", chr(937))  # Ω
# print("Emoji rocket (code point 128640):", chr(128640))          # 🚀

# # Print a range of Unicode characters (e.g., 945–950: Greek lowercase)
# print("Greek lowercase letters (Unicode 945 to 950):")
# for code in range(945, 951):
#     print(f"{code}: {chr(code)}", end=' ')


#           -----------------------------------------------------------------

# Write a Python program to create a bytearray from a list.

# int_list = [65, 66, 67, 68, 69]  # Corresponds to 'ABCDE'

# byte_arry = bytearray(int_list)

# print(f"Byte array : {byte_arry}")

# print(f"To string conversion",byte_arry.decode('utf-8'))  # # decode to convert into string 

#       -----------------------------------------------------------------

# Write a Python program to round a floating-point number to a specified number of decimal places.


# number = float(input("Enter a floating-point number: "))
# decimals = int(input("Enter the number of decimal places to round to: "))


# rounded_num = round(number, decimals)

# print(f"Rounded number: {rounded_num}")

#   # print(f"Rounded number: {rounded_num:.{decimals}f}")

#           --------------------------------------------------------------------------------------------

# Write a Python program to format a specified string and limit the length of a string.


# text = input("Enter a string: ")
# max_length = int(input("Enter maximum length to display: "))

# limited_text = text[:max_length]

# print(f"Formatted (max {max_length} chars): '{limited_text}'")

#  # print("{:.10}".format(text))       # First 10 characters
#  # print(f"{text:.10}")               # First 10 characters using f-string

#           -----------------------------------------------------

# Write a Python program to determine if a variable is defined or not.


# var_name = "my_var"

# my_var = 42   # Optionally define the variable (uncomment the next line to test)

# if var_name in globals() or var_name in locals():
#     print(f"Variable '{var_name}' is defined.")
# else:
#     print(f"Variable '{var_name}' is NOT defined.")

#           --------------------------------------------------

# Write a Python program to determine the largest and smallest integers, longs, and floats.

# import sys

# print("FLOAT VALUES (using sys.float_info):")
# print("Maximum float value:", sys.float_info.max)
# print("Minimum positive float value:", sys.float_info.min)
# print("Float precision (digits):", sys.float_info.dig)

# print("\nINTEGER VALUES:")
# print("Python integers have arbitrary precision.")
# print("Example large int:", 10**100)
# print("Example small int:", -10**100)

#       ----------------------------------------------------------------

# Write a Python program to check whether multiple variables have the same value.


# a = 10
# b = 10
# c = 10

# if a == b == c:
#     print("All variables have the same value.")
# else:
#     print("Variables have different values.")

#       ----------------------------------------------------------------

# Write a Python program to sum all counts in a collection.

# from collections import Counter

# item_counts = Counter({'apples': 4, 'bananas': 7, 'oranges': 3})

# # Sum all the counts
# total = sum(item_counts.values())

# print("Total count of all items:", total)

#           ----------------------------------------------------------------


# Write a Python program to check whether lowercase letters exist in a string.

# def contains_lowercase(s):
#     for char in s:
#         if char.islower():
#             return True
#     return False

# input_string = input("Enter a string: ")

# if contains_lowercase(input_string):
#     print(f"Input string --->  {input_string} --- string contains lowercase")
# else:
#     print("The string does not contain lowercase")

#       -------------------------------------------------------------------------

# Write a Python program to add leading zeroes to a string.

# def add_leading_zeros(input_strings, total_length):
#     return input_strings.zfill(total_length)        #  zfill to pads the string with leading zeroes until it reaches the specified length.



# original_length = input("Enter a string: ")
# desired_length = int(input("Enter a total length with leading zeros: "))

# result = add_leading_zeros(original_length, desired_length)
# print("Result with leading zeros: ",result)

#           -----------------------------------------------------------------------------

# Write a Python program that uses double quotes to display strings.

# greeting = "Hello, world!"
# name = "Sanket"
# message = "Welcome to Python programming."

# print("Greeting:", greeting)
# print("Name:", name)
# print("Message:", message)

#           ------------------------------------------------------

#       # # 132     --------------------------------------------------------

# Write a Python program to split a variable length string into variables.


# def split_string_to_variables(input_string, delimiter=' '):         # the function splits the string using a space ' '. You can change this to a comma ',', tab '\t',
#     parts = input_string.split(delimiter)
    
#     return parts

# input_string = input("Enter a string (e.g., 'apple banana cherry'): ")
# variables = split_string_to_variables(input_string)

# print("Splitted values:")
# for i, value in enumerate(variables):   #  enumerate(variables) returns each value in the list along with its index.
#     print(f"Variable {i + 1}: {value}")



#               ---------------------------------------------------------------------------

# Write a Python program to input two integers on a single line.


# a, b = map(int, input("Enter two integers separated by space: ").split())  # #  map(int, ------> converts each string to an integer.

# print("First integer:", a)
# print("Second integer:", b)

#           ------------------------------------------------------------

# Write a Python program to calculate the time runs (difference between start and current time) of a program.

# import time

# start_time = time.time()

# print("Program is running...")
# time.sleep(5)  # Wait for 5 seconds as an example   #  time.sleep(5) simulates a delay (replace it with your actual processing).


# # Record the end time (current time)
# end_time = time.time()

# # Calculate the difference
# run_time = end_time - start_time

# print(f"Time elapsed: {run_time:.2f} seconds")

#               ---------------------------------------------------------------


# Write a Python program to print a variable without spaces between values.
# Sample value : x =30
# Expected output : Value of x is "30"

# x = 30
# print(f'Value of x is "{x}"')

#           --------------------------------------------------------


# Write a Python program to extract a single key-value pair from a dictionary into variables.

# my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# key, value = next(iter(my_dict.items()))        # next gets the first item from the iterator

# print("Key:", key)
# print("Value:", value)

# key_to_extract = 'city'
# key, value = key_to_extract, my_dict[key_to_extract]
# print("Key:", key)
# print("Value:", value)

#               -------------------------------------------------------------

# Write a Python program to convert true to 1 and false to 0.

# # Boolean values
# a = True
# b = False

# # Convert to integers
# a_int = int(a)
# b_int = int(b)

# # Print the results
# print(f"True as integer: {a_int}")
# print(f"False as integer: {b_int}")


#               -------------------------------------------------------------

# Write a Python program to convert an integer to binary that keeps leading zeros.
# Sample data : x=12
# Expected output : 00001100
# 0000001100

# x = 12

# binary_8_bit = format(x, '08b')    #  binary format (b), 8 digits, zero-padded.
# binary_10_bit = format(x, '010b')

# print("8-bit binary:", binary_8_bit)
# print("10-bit binary:", binary_10_bit)

#           -----------------------------------------------------------------------------

# Write a python program to convert decimal to hexadecimal.
# Sample decimal number: 30, 4
# Expected output: 1e, 04

#               -----------------------------------------------------

#           # #  143   ---------------------------------

# Write a Python program to check whether a variable is an integer or string.

# x = 18
# y = "Sanket"
# z = 3.14


# def check_variable_type(var):
#     if isinstance(var, int):
#         print(f"The variable '{var}' is an Integer.")
#     elif isinstance(var, str):
#         print(f"The variable '{var}' is an String.")
#     else:
#         print(f"The variable is neither an Integer nor a String.")

# check_variable_type(x)
# check_variable_type(y)
# check_variable_type(z)

#               ---------------------------------------------------------------------

# Write a Python program to test if a variable is a list, tuple, or set.


# def check_data_type(var):
#     if isinstance(var, list):
#         print(f"The variable '{var}' is an List.")
#     elif isinstance(var, tuple):
#         print(f"The variable '{var}' is an Tuple.")
#     elif isinstance(var, set):
#         print(f"The variable '{var}' is an Set.")
#     else:
#         print(f"The variable '{var}' is not a List, Tuple, or Set.")

# a = [1, 2, 3]
# b = (4, 5, 6)
# c = {7, 8, 9}
# d = "Sanket"

# check_data_type(a)
# check_data_type(b)
# check_data_type(c)
# check_data_type(d)

#           # # 146  ---------------

#                   ---------------------------------------------------------------

# Write a Python function to check whether a number is divisible by another number. Accept two integer values from the user.


# def is_divisible(a, b):
#     if b == 0:
#         return "Division by zero is not allowed"
#     elif a % b == 0:
#         print(f"{a} is divisible by {b}")
#     else:
#         print(f"{a} is NOT divisible by {b}.")
    
# try:

#     num1 = int(input("Enter the first integer: "))
#     num2 = int(input("Enter the second integer: "))


#     result = is_divisible(num1, num2)

#     print(result)

# except ValueError:
#     print("Please enter valid integers.")

#           ------------------------------------------------------------------

