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
#             balance = balance + amount
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
#             balance = balance - amount
#             print(f"₹{amount} withdrawn. New balance: ₹{balance}")

#     elif choice == '3':
#         print(f"Your current balance is: ₹{balance}")

#     elif choice == '4':
#         # Placeholder for future loan feature
#         print("Loan feature coming soon!")
#         pass  # TODO: Implement loan feature later

#     elif choice == '5':
#         print("Thank you for banking with us. Goodbye")
#         break  # Exit the loop and program

#     else:
#         print("Invalid choice. Please enter a number between 1 and 5.")
#         continue  # Ask the user again


#       ---------------------------------------------------------------------------

# Ask 5 multiple-choice questions.

# For each wrong answer, print "Wrong! Try again." and continue to the next question.

# If the user types "quit", break the game.

# Use pass for a future "hint system".

# List of questions and answers

# questions = [
#     {
#         "question": "1. What is the capital of France?\n(a) Berlin\n(b) Madrid\n(c) Paris\n(d) Rome",
#         "answer": "c"
#     },
#     {
#         "question": "2. Which planet is known as the Red Planet?\n(a) Earth\n(b) Mars\n(c) Jupiter\n(d) Venus",
#         "answer": "b"
#     },
#     {
#         "question": "3. What is the largest ocean on Earth?\n(a) Atlantic\n(b) Indian\n(c) Arctic\n(d) Pacific",
#         "answer": "d"
#     },
#     {
#         "question": "4. Which language is used to write Python?\n(a) English\n(b) C\n(c) Python\n(d) Java",
#         "answer": "c"
#     },
#     {
#         "question": "5. What is the square root of 64?\n(a) 6\n(b) 8\n(c) 7\n(d) 9",
#         "answer": "b"
#     }
# ]

# print("Welcome to the Quiz Game!")
# print("Type 'quit' anytime to exit.")
# print("Type 'hint' to get a hint (feature coming soon).\n")

# score = 0

# for q in questions:
#     print(q["question"])
#     user_answer = input("Your answer (a/b/c/d): ").lower()

#     if user_answer == "quit":
#         print("Game exited by user.")
#         break

#     if user_answer == "hint":
#         # Future hint system placeholder
#         print("Hint system coming soon!")
#         pass
#         user_answer = input("Try again (a/b/c/d): ").lower()
#         if user_answer == "quit":
#             print("Game exited by user.")
#             break

#     if user_answer == q["answer"]:
#         print("Correct!\n")
#         score += 1
#     else:
#         print("Wrong! Try again.\n")

# print(f"\nYour final score: {score}/{len(questions)}")
# print("Thanks for playing!")

#       -------------------------------------------------------------

# User chooses from 3 patterns (triangle, square, pyramid).

# Use for loops to generate the patterns.

# Use continue to skip invalid sizes and break if the user chooses "exit".

# while True:
#     print("\nChoose a pattern to print:")
#     print("1. triangle")
#     print("2. square")
#     print("3. pyramid")
#     print("Type 'exit' to quit.")
    
#     choice = input("Enter your choice: ").lower()  # Needs string input first for user choice

#     if choice == 'exit':
#         print("Exiting the program.")
#         break

#     size = int(input("Enter the size of the pattern (positive number): "))

#     if size <= 0:
#         print("Invalid size. Please enter a positive number.")
#         continue  # Skip to next loop iteration

#     if choice == 'triangle':
#         print("\nTriangle Pattern:")
#         for i in range(1, size + 1):
#             print("*" * i)

#     elif choice == 'square':
#         print("\nSquare Pattern:")
#         for i in range(size):
#             print("*" * size)

#     elif choice == 'pyramid':
#         print("\nPyramid Pattern:")
#         for i in range(1, size + 1):
#             spaces = ' ' * (size - i)
#             stars = '*' * (2 * i - 1)
#             print(spaces + stars)

#     else:
#         print("Invalid pattern choice. Please try again.")
#         continue  # Repeat the loop


#       -------------------------------------------------------------------------

# A list of available books is displayed.

# User can borrow, return, or view books.

# break to exit the system.

# continue when the user enters a wrong book name.

# pass for a "late fee calculator" feature to be added later.


# # # Initial list of available books
# available_books = ["1984", "To Kill a Mockingbird", "The Great Gatsby", "Pride and Prejudice"]

# # Borrowed books list
# borrowed_books = []

# def display_books():
#     print("\nAvailable Books:")
#     if not available_books:
#         print("No books currently available.")
#     else:
#         for book in available_books:
#             print("-", book)

# def borrow_book():
#     book = input("Enter the name of the book you want to borrow: ")
#     if book in available_books:
#         available_books.remove(book)
#         borrowed_books.append(book)
#         print(f"You borrowed '{book}'.")
#     else:
#         print("Book not available. Please check the title.")
#         continue_flag = True
#         return continue_flag
#     return False

# def return_book():
#     book = input("Enter the name of the book you want to return: ")
#     if book in borrowed_books:
#         borrowed_books.remove(book)
#         available_books.append(book)
#         print(f"You returned '{book}'.")
#     else:
#         print("This book wasn't borrowed from this library.")
#         continue_flag = True
#         return continue_flag
#     return False

# def late_fee_calculator():
#     # Feature to be implemented later
#     pass

# # Main loop
# while True:
#     print("\nLibrary Menu:")
#     print("1. View Books")
#     print("2. Borrow Book")
#     print("3. Return Book")
#     print("4. Calculate Late Fee (Coming Soon)")
#     print("5. Exit")

#     choice = input("Enter your choice (1-5): ")

#     if choice == "1":
#         display_books()
#     elif choice == "2":
#         if borrow_book():
#             continue
#     elif choice == "3":
#         if return_book():
#             continue
#     elif choice == "4":
#         late_fee_calculator()
#         print("Late fee calculator feature will be added soon.")
#     elif choice == "5":
#         print("Exiting the system. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please select from 1 to 5.")
#         continue


#           -----------------------------------------------------------------------------------------------