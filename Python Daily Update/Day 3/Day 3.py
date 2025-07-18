# Section 1: Built-in Data Types (int, float, str, list, tuple, dict, bool, set)
# Check Data Type:
# Ask the user to enter a value and print its data type. Then determine if it’s a number or not.
# -------------------------------------------------------------------------------------------------------
# Dynamic Type Detector:
# Take three inputs from the user and detect which one is integer, float, or string using type() and conditionals.
# -------------------------------------------------------------------------------------------------------

# x = ("Sanket Salunke")		
# x = int(10)		
# x = float(10.5)     #float	
# x = complex(5j)
# print(type(x))

# value = input("Enter a value: ")

# try:
#     int_val = int(value)
#     print("Data type is:", type(int_val))
#     print("This is a number (int).")
# except ValueError:
#     try:
#         float_val = float(value)
#         print("Data type is:", type(float_val))
#         print("This is a number (float).")
#     except ValueError:
#         print("Data type is:", type(value))
#         print("This is NOT a number.")
#     try:
#         string_val = str(value)
#         print("Data type is:", type(str))
#         print("This is a number (string).")
#     except ValueError:
#         print("Data type is:", type(value))
#         print("This is string.")
#     try:
#         complex_val = str(value)
#         print("Data type is:", type(complex))
#         print("This is a number (complex).")
#     except ValueError:
#         print("Data type is:", type(value))
#         print("This is complex.")

#             ------------------------------

# 🔹 Section 2: Setting Specific Data Types / Type Conversion
# Type Conversion Challenge:
# Input 2 numbers as strings and add them as:

# Strings (concatenation)

# Integers (sum)

# Floats (sum)

# Section 2: Type Conversion Challenge

# # Input as strings
# str_num1 = input("Enter first number (as string): ")
# str_num2 = input("Enter second number (as string): ")

# # For String concatenation
# concat_result = str_num1 + str_num2
# print("String concatenation:", concat_result)


# For Integer addition

# # Input as strings
# int_num1 = input("Enter first number (as value): ")
# int_num2 = input("Enter second number (as value): ")

# try:
#     int_sum = int(int_num1) + int(int_num2)
#     print("Integer sum:", int_sum)
# except ValueError:
#     print("Cannot convert to integers.")

# # For Float addition
# try:
#     float_sum = float(int_num1) + float(int_num2)
#     print("Float sum:", float_sum)
# except ValueError:
#     print("Cannot convert to floats.")

#  -------------------------------------------------

# Temperature Converter:
# Take temperature in Celsius from the user, convert to Fahrenheit and Kelvin using correct type conversions.


# Temperature Converter

# celsius_input = input("Enter temperature in Celsius: ")

# try:
#     # Convert to float
#     celsius = float(celsius_input)
    
#     # Conversion formulas
#     fahrenheit = (celsius * 9/5) + 32
#     kelvin = celsius + 273.15
    
#     # Display results
#     print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")
#     print(f"Temperature in Kelvin: {kelvin:.2f}K")
    
# except ValueError:
#     print("Invalid input. Please enter a valid number for temperature.")

#  --------------------------------------------------------------------------------

# Year and Age Logic:
# Take user’s birth year (as string), convert to integer, and calculate their age assuming the current year is 2025.

# Year and Age Logic

# birth_year_input = input("Enter your birth year: ")

# try:
#     # Convert to integer
#     birth_year = int(birth_year_input)
    
#     # Assume current year is 2025
#     current_year = 2025
    
#     # Calculate age
#     age = current_year - birth_year

#     # Display result
#     print(f"You are {age} years old in {current_year}.")
    
# except ValueError:
#     print("Invalid input. Please enter a valid birth year.")

#  --------------------------------------------------------------

# Add Two Numbers Function:
# Create a program that takes two floats and returns their rounded sum. Use proper type hinting.

# def add_and_round(num1: float, num2: float) -> float:
#     """
#     Adds two float numbers and returns the rounded sum (to 2 decimal places).
#     """
#     return round(num1 + num2, 2)

# # Get user input
# try:
#     number1 = float(input("Enter the first number: "))
#     number2 = float(input("Enter the second number: "))
    
#     result = add_and_round(number1, number2)
#     print(f"Rounded sum: {result}")

# except ValueError:
#     print("Invalid input. Please enter valid floating-point numbers.")

#  ----------------------------------------------------------------------


# Area Calculator:
# Write a program to calculate the area of a rectangle. Accept length and width as floats. Use -> float in return.


# def calculate_area(length: float, width: float) -> float:
#     """
#     Calculates and returns the area of a rectangle.
#     """
#     return length * width

# # Input from user
# try:
#     length = float(input("Enter the length of the rectangle: "))
#     width = float(input("Enter the width of the rectangle: "))
    
#     area = calculate_area(length, width)
#     print(f"Area of the rectangle: {area} square units")

# except ValueError:
#     print("Invalid input. Please enter valid float values for length and width.")

#  ---------------------------------------------------------------------------------------

# Student Info Storage:
# Accept name, roll_no, and marks from the user. Use type annotations and store in a dictionary.


# def get_student_info(name: str, roll_no: int, marks: float) -> dict:
#     """
#     Returns a dictionary containing student information.
#     """
#     return {
#         "name": name,
#         "roll_no": roll_no,
#         "marks": marks
#     }

# # Collect user input
# try:
#     student_name = input("Enter student's name: ")
#     student_roll_no = int(input("Enter roll number: "))
#     student_marks = float(input("Enter marks: "))

#     student_data = get_student_info(student_name, student_roll_no, student_marks)
#     print("Student Information:")
#     print(student_data)

# except ValueError:
#     print("Invalid input. Make sure roll number is an integer and marks are a number.")

#   ---------------------------------------------------------------------------------

# Formatted Receipt Generator:
# Accept item name (str), quantity (int), and price (float). Calculate total and display the receipt with formatted output.
