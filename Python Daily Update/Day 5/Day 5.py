
# 1. Even or Odd: Ask the user for a number and check if it is even or odd.

# number = int(input("Enter a number: "))

# # To Check if the number is even or odd
# if number % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

# 2. Positive, Negative, or Zero: Take a number and check whether it is positive, negative, or zero.

#number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
# if number > 0:
#     print("The number is positive.")
# elif number < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")



# 3. Voting Eligibility: Ask user's age and tell if they are eligible to vote (age >= 18).

# age = int(input("enter the age"))

# if age > 18 :
#     print(f"Congratulation you are age is {age}")
# else :
#     print(f"Oops sorry you are not eligible for vote your age is {age}")

#       ------------------------------------------------------------------------

# tuple = {1,2,3}
# dict = {'a':1,'b':2,'c':4}
# set=(1,2,3,4)
# list=[1,2,4,5,1]
# list.append(12)
# print(list)
# print(list[:3])

#       -------------------------------------------------------------------------

# 3. Voting Eligibility: Ask user's age and tell if they are eligible to vote (age >= 18).

# age = float(input("Enter your age: "))

# # To Check voting eligibility
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote yet.")

#       ------------------------------------------------------------------------------------------

# 4. Greatest of Two Numbers: Input two numbers and print which one is greater or if they are equal.

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# # Compare the two numbers
# if num1 > num2:
#     print(f"{num1} is greater than {num2}.")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}.")
# else:
#     print("Both numbers are equal.")

#           -------------------------------------------------

# 5. Pass or Fail: Ask marks out of 100. Print Pass if marks >= 40, else Fail.

# marks = float(input("Enter your marks (out of 100): "))

# if marks >= 40:
#     print("User is Pass")
# else:
#     print("User is Fail")

#       -----------------------------------------------------------

# 6. Simple Login Check: Ask username and password. If username='admin' and password='1234',

# username = input("Enter yourname:")
# password = input("Enter password:")

# if username == "admin" and password=="1234":
#     print("Login Successfull")
# else:
#     print("Invalid user or password")

# simple programm not used import function

#       ----------------------------------------

# 7. Leap Year Checker: Input a year and check if it is a leap year.

# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

#       ---------------------------------------------------------

#  8. Ticket Price Calculator: Age <5: free, 5-12: Rs 50, >12: Rs 100.

# age = int(input("Enter your age: "))

# if age < 5:
#     print("Ticket is free")
# elif age <=12:
#     print("Ticket price is 50")
# else:
#     print ("Ticket price is 100")

#       --------------------------------------------------------

# 9. Character Case Checker: Check if a character is uppercase, lowercase, digit, or special
# character.

# char = input("Enter a character: ")

# if len(char) != 1:
#     print("Please enter exactly one character.")
# else:
#     if char.isupper():
#         print("Uppercase letter.")
#     elif char.islower():
#         print("Lowercase letter.")
#     elif char.isdigit():
#         print("Digit.")
#     else:
#         print("Special character.")

#       -----------------------------------------------------------

#     10. Number Guessing Game: Secret number = 7. Ask user to guess and check.
 
# from dev.config import Password,USERNAME,Secret_number

# value = int(input("Guess the secret number (between 1 and 10): "))

# guess=int(input("guess a number between 1 to 10:"))

# # if guess == Secret_number:
# #     print("you guessed it right")
# # else:
# #     print("you guessed it wrong")

# password=int(input("enter your password"))
# username=input("enter your username")
# if password ==Password and username==USERNAME:
#     print("access granted")
# else:
#     print("access denied")

# need to discuss about import 

#       -----------------------------------

# 11. Electricity Bill: Units <=50: Rs 2/unit; 51-150: Rs 3/unit; above 150: Rs 5/unit.

# # Ask user for number of units
# units = int(input("Enter electricity units consumed: "))

# if units <= 50:
#     bill = units * 2
# elif units <= 150:
#     # bill = (50 * 2) + (units - 50) * 3
#     bill = units * 3
# else:
#     # bill = (50 * 2) + (100 * 3) + (units - 150) * 5
#     bill = units * 5

# print(f"Total electricity bill: ₹{bill}")

#           ----------------------------------

# 12. Discount & GST: Apply 10% discount and then add 18% GST to original price.

# # Ask user for the original price
# original_price = float(input("Enter the original price: ₹"))

# # Step 1: Apply 10% discount
# discount = original_price * 0.10
# discounted_price = original_price - discount

# # Step 2: Add 18% GST
# gst = discounted_price * 0.18
# final_price = discounted_price + gst

# # Display the final price
# print(f"\nOriginal Price: ₹{original_price:.2f}")
# print(f"Discount (10%): -₹{discount:.2f}")
# print(f"Price after discount: ₹{discounted_price:.2f}")
# print(f"GST (18%): +₹{gst:.2f}")
# print(f"Final Price to Pay: ₹{final_price:.2f}")

#  need to check this ₹{final_price:.2f}") with meaning

#       --------------------------------------------------

# 13. Second Largest: Find second largest among three numbers.

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))

# if (a > b and a < c) or (a > c and a < b):
#     second_largest = a
# elif (b > a and b < c) or (b > c and b < a):
#     second_largest = b
# else:
#     second_largest = c

# print(f"The second largest number is: {second_largest}")

#           ---------------------------------------------

# BMI Calculator: BMI = weight/(height^2). Classify as Underweight (<18.5), Normal (18.5-24.9),
# Overweight (>=25).

# # Get weight and height from user
# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in meters: "))

# # Calculate BMI
# bmi = weight / (height ** 2)

# print(f"\nYour BMI is: {bmi:.2f}")

# if bmi < 18.5:
#     print("Category: Underweight")
# elif 18.5 <= bmi <= 24.9:
#     print("Category: Normal")
# else:
#     print("Category: Overweight")

# ***************************** 

#       ---------------------------------------------------

# 15. Grade Calculator: Average marks of 5 subjects: A >=90, B >=75, C >=50, Fail <50.


# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     print("Grade A")

# elif marks >= 75:
#     print("Grade B")

# elif marks >= 50:
#     print("Grade C")
# else:
#     print("Fail")

#       ------------------------------------------------------

# 16. ATM Simulation: Ask balance and amount. Deduct only if balance is sufficient.

# balance = float(input("Enter your current balance: ₹"))
# withdraw = float(input("Enter amount to withdraw: ₹"))

# #To Check and update balance
# if withdraw <= balance:
#     balance = balance - withdraw        #balance -= withdraw  #     balance = balance - withdraw  # 
#     print(f"Withdrawal successful! Remaining balance: ₹{balance:.2f}")
# else:
#     print("Insufficient balance.")

#           -------------------------------------------------------------

#17. Triangle Checker: Check if three sides form a valid triangle. If valid, print type: Equilateral,
# Isosceles, or Scalene.

# Input three sides of the triangle

# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))
# c = float(input("Enter side c: "))

# if a + b > c and b + c > a and c + a > b:
#     print("This is a valid triangle.")
    
#     if a == b == c:
#         print("Type: Equilateral triangle")
#     elif a == b or b == c or c == a:
#         print("Type: Isosceles triangle")
#     else:
#         print("Type: Scalene triangle")
# else:
#     print("Not a valid triangle.")


#       --------------------------------------------------------

# 18. Rock-Paper-Scissors: User vs computer. Decide winner.

# import random

# choices = ["rock","paper","scissors"]

# user = input("Enter your choice (rock, paper, scissors): ").lower()

# computer = random.choice(choices)
# print(f"Coumputer chose {computer}")

# if user == computer: 
#     print("It's a tie.")
# elif    (user == "rock" and computer == "scissors") or \
#         (user == "scissors" and computer == "paper") or \
#         (user == "paper" and computer == "rock"): 
#         print("You won")

# elif user in choices:
#       print("Computer wins")
# else:
#       print("Invalid Input.")

#           ---------------------------------------------------------------

# 19. Movie Ticket: Ask age and time. Apply 20% discount if student (<18).

# ticket_price = 400

# age = int(input("Enter your age: "))
# time = input("Enter show time (as 09:30 PM): ")

# if age < 18:
#     discount = ticket_price * 0.20
#     final_price = ticket_price - discount
#     print("Discount is applied for student 20%")
# else :
#     final_price = ticket_price

# print(f"show time : {time}")
# print(f"Ticket price : rs {final_price}")


# 20. Traffic Signal: Ask color. Green: Go, Red: Stop, Yellow: Wait.

# colour = input("Enter traffic signal colour (Red, Green, Yellow): ").lower()

# if colour == "green":
#     print("Go")
# elif colour == "red":
#     print("Stop")
# elif colour == "yellow":
#     print("Wait")
# else:
#     print("Invalid input!")

#       ------------------------------------------------------------------

