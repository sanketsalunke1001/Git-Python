# Print all prime numbers between 1 and 100 using a for loop.


# print("Prime numbers between 1 and 100:")
# for num in range(2, 101):  # Start from 2, as 1 is not prime
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=" ")

#   -----------------------------------------------------

# Write a program to print a multiplication table for a number entered by the user.

# num = int(input("Enter number to print its Multiplication table: "))
# print(f"\nMultiplication Table for {num}:")
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")

#--------------------------

# num1 = int(input("Enter number to print its Multiplication table: "))

# num2 = int(input("Enter number to print its Multiplication table: "))

# sum = num1 * num2

#       ----------------------------------------------------

# Count and display how many vowels are in a given string using a for loop.


# text = input("Enter a string: ")
# vowels = "Sanket_Salunke"
# count = 0

# for char in text:
#     if char in vowels:
#         count += 1

# print(f"Number of vowels in the string: {count}")

#       ------------------------------------------------------

# Print a pattern like this using a for loop:
# *
# **
# ***
# ****

# rows = 4  # Number of rows in the pattern

# for i in range(1, rows + 1):
#     print("*" * i)

#       --------------------------------------------------------

# Write a program to reverse a string without using slicing, only with a for loop.

# text = input("Enter a string: ")
# reversed_text = ""

# for char in text:
#     reversed_text = char + reversed_text  # Add character to the front

# print("Reversed string:", reversed_text)


# Create a list of 10 numbers and print the sum of only even numbers using for loop and continue.

# numbers = [1, 3, 5, 6, 18, 8, 12, 5, 7, 2, 10, 13, 4, 6]
# even_sum = 0

# for num in numbers:
#     if num % 2 != 0:
#         continue  # Skip odd numbers
#     even_sum += num

# print("Sum of even numbers:", even_sum)

#       ------------------------------------------------------------------


# Generate the Fibonacci sequence up to the first 15 numbers using for loop.






