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
