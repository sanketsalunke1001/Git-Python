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
#
# Generate the Fibonacci sequence up to the first 15 numbers using for loop.

# n1 = 0
# n2 = 1

# print("Fibonacci sequence (first 15 numbers):")

# for i in range(15):
#     next_number = n1 + n2
#     n1 = n2
#     n2 = next_number
#     print(n1, end=" ")

#       -----------------------------------------------------

# Keep asking the user for input until they type "exit", then stop using a while loop.

# while True:
#     user_input = input("Enter something (type 'exit' to stop): ")
    
#     if user_input.lower() == "exit":
#         print("Exiting the program.")
#         break
    
#     print(f"You entered: {user_input}")

#       ------------------------------------------------------------------

# Write a program to check if a number is an Armstrong number, using a while loop.

# num = int(input("Enter a number: "))
# original = num
# n = len(str(num))  # Number of digits
# sum_of_powers = 0

# while num > 0:
#     digit = num % 10
#     sum_of_powers =sum_of_powers + digit ** n
#     num = num // 10

# # Check if Armstrong
# if sum_of_powers == original:
#     print(f"{original} is an Armstrong number.")
# else:
#     print(f"{original} is NOT an Armstrong number.")

#       ---------------------------------------------------

# Find the factorial of a number using a while loop.

# num = int(input("Enter a number to find its factorial: "))

# # Factorial is not defined for negative numbers
# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     factorial = 1
#     i = 1

#     while i <= num:
#         factorial *= i  # Multiply factorial by i
#         i += 1          # Increment i

#     print(f"Factorial of {num} is {factorial}")

#       ---------------------------------------------------

# Use a while loop to keep dividing a number by 2 until it becomes less than 1, and print the number of divisions.


# # Input from the user
# num = float(input("Enter a number: "))
# count = 0

# # Keep dividing by 2 until the number is less than 1
# while num >= 1:
#     num = num / 2
#     count = count + 1

# # Print the result
# print("Number of divisions performed:", count)

#       ----------------------------------------------------------

# Write a program that keeps asking for a password until the correct password ("python123") is entered.


# correct_password = "python123"

# while True:
#     entered_password = input("Enter Password: ")

#     if entered_password == correct_password:
#         print("Access Granted")
#     else:
#         print("Incorrect password")

#       ------------------------------------------------

# Write a program to display numbers from 1 to 50, but stop the loop if the number is divisible by both 3 and 7 using break.

# for num in range (1, 51):
#     if num % 3 == 0 and num % 7 == 0:
#         print(f"{num} is divisible by 3 and 7. stopping loop")
#         break
# print(num)

#   ----------------------------------------------------------------------

# Print all numbers between 1 and 30, skipping those that are divisible by 4 using continue.

# num = int(input("Enter "))

# for num in range(1, 31):
#     if num % 4 == 0:
#         continue  # Skip numbers divisible by 4
#     print(f"\t{num} Number which were divisible by 4")


#       --------------------------------------------------------

# Write a program where pass is used inside a loop as a placeholder for a future feature (e.g., add a feature later when the number is negative).

# while True:
#     num = int(input("Enter a number (0 to stop): "))

#     if num == 0:
#         print("Exiting the program.")
#         break

#     if num < 0:
#         # Placeholder for future negative number handling
#         pass  # TODO: Add feature for negative numbers later
#     else:
#         print(f"You entered a positive number: {num}")

#       --------------------------------------------------------------------

# Start with an account balance (e.g., ₹5000).

# Menu-driven using while loop:

# Deposit money

# Withdraw money

# Check balance

# Exit

# Use break to exit, continue for invalid choices, and pass for a "loan feature coming soon".

# balance = 5000  # Starting balance

# while True:
#     print("\n--- Bank Menu ---")
#     print("1. Deposit Money")
#     print("2. Withdraw Money")
#     print("3. Check Balance")
#     print("4. Loan Feature (Coming Soon)")
#     print("5. Exit")

#     choice = input("Enter your choice (1-5): ")

#     if choice == '1':
#         amount = float(input("Enter amount to deposit: ₹"))
#         if amount > 0:
#             balance += amount
#             print(f"₹{amount} deposited. New balance: ₹{balance}")
#         else:
#             print("Invalid amount. Must be greater than zero.")

#     elif choice == '2':
#         amount = float(input("Enter amount to withdraw: ₹"))
#         if amount > balance:
#             print("Insufficient balance!")
#         elif amount <= 0:
#             print("Invalid amount. Must be greater than zero.")
#         else:
#             balance -= amount
#             print(f"₹{amount} withdrawn. New balance: ₹{balance}")

#     elif choice == '3':
#         print(f"Your current balance is: ₹{balance}")

#     elif choice == '4':
#         # Placeholder for future loan feature
#         print("Loan feature coming soon!")
#         pass  # TODO: Implement loan feature later

#     elif choice == '5':
#         print("Thank you for banking with us. Goodbye!")
#         break  # Exit the loop and program

#     else:
#         print("Invalid choice. Please enter a number between 1 and 5.")
#         continue  # Ask the user again
