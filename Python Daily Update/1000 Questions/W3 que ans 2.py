# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

# def all_unique(sequence):

#     return len(sequence)  == len(set(sequence))

# # sequence = [1, 2, 3, 4]

# print(all_unique([1, 2, 3, 4]))         # return true

# print(all_unique([1, 2, 2, 3, 4, 5]))  # reurn false

#           -------------------------------------------------------------

# Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once.

# import itertools

# def genereate_unique_string():
#     characters = ['a', 'e', 'i', 'o', 'I']
#     permutations = itertools.permutations(characters)   #  #        generates all possible orderings of the characters.
#     strings = [''.join(p) for p in permutations]        #  #       converts each tuple of characters into a string.
#     return strings

# all_strings = genereate_unique_string()
# for s in all_strings:
#     print(s)

# print(f" Total unique strings: {len(all_strings)}")


#                       ---------------------------------------------------------------------


# Write a Python program that removes and prints every third number from a list of numbers until the list is empty.

# def remove_every_third(numbers):

#     index = 0
#     while numbers:
#         index = (index + 2) % len(numbers)
#         removed = numbers.pop(index)
#         print(f"removed : {removed}")

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# remove_every_third(nums)

#           --------------------------------------------------------

#           #  4

#  Write a Python program to make combinations of 3 digits.

# import itertools

# def generate_combinations():
#     digits = range(6)
#     combinations = itertools.combinations(digits, 3)

#     for combo in combinations:
#         print(combo)

# generate_combinations()

#       ------------------------------------------------------------

# Write a Python program that prints long text, converts it to a list, and prints all the words and the frequency of each word.


# import string

# def word_frequency(text):
#     text = text.lower()
#     text = text.translate(str.maketrans('','',string.punctuation))  # removes all punctuation marks (like ., etc.), ensuring that words like "Python." and "python" are treated as the same word.

#     words = text.split()  # method splits the text into a list of words, separating by spaces.

#     frequency = {}  #  to store the word counts.


#     for word in words:
#         if word in frequency:
#             frequency[word] += 1
#         else:
#             frequency[word] = 1

#     for word, count in frequency.items():
#          print(f"{word}: {count}")

# text = """A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are 'case-sensitive' (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords."""

# word_frequency(text)

#               -----------------------------------------------------

#       #  #   7 8

# Write a Python program to get a list of locally installed Python modules.

# import sys

# if sys.version_info >= (3, 8):
#     from importlib.metadata import distributions

#     def list_installed_modules():
#         for dist in distributions():
#             print(f"{dist.metadata['Name']}=={dist.version}")

#     list_installed_modules()
# else:
#     print("This method requires Python 3.8 or higher.")


#                   --------------------------------------------------------------

# Write a Python program to display some information about the OS where the script is running.

# import os
# import platform

# def display_os_info():
#     print("Operating System Information")
#     print("----------------------------")
#     print(f"System       : {platform.system()}")
#     print(f"Node Name    : {platform.node()}")
#     print(f"Release      : {platform.release()}")
#     print(f"Version      : {platform.version()}")
#     print(f"Machine      : {platform.machine()}")
#     print(f"Processor    : {platform.processor()}")
#     print(f"Architecture : {platform.architecture()[0]}")
#     print(f"OS Name (os.name): {os.name}")


# display_os_info()

#               --------------------------------------------------------------


# Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to a target value. Print all those three-element combinations.
# Sample data:
# /*
# X = [10, 20, 20, 20]
# Y = [10, 20, 30, 40]
# Z = [10, 30, 40, 20]
# target = 70


# def find_triplets(X, Y, Z, target):
#     print(f"Triplets that sum to {target}")
#     found = False


#     for x in X:
#         for y in Y:
#             for z in Z:
#                 if x + y + z == target:
#                     print(f"({x}, {y}, {z})")

#                     found = True
                
#     if not found:
#         print("No triplets were found")

# X = [10, 20, 20, 20]
# Y = [10, 20, 30, 40]
# Z = [10, 30, 40, 20]

# target = 70

# find_triplets(X, Y, Z, target)

#           -----------------------------------------------------------

# Write a Python program that generates a list of all possible permutations from a given collection of distinct numbers.


# import itertools

# def generate_permutations(numbers):
#     perms = list(itertools.permutations(numbers))
#     print(f"All permutations of {numbers}")

#     for p in perms:
#         print(p)
    
# numbers = [5, 7, 9]

# # generate_permutations(numbers)
# print(f"generate_permutations(numbers): {generate_permutations(numbers)}")

#               -------------------------------------------------------------

# Write a Python program to get all possible two-digit letter combinations from a 1-9 digit string.
# string_maps = {
# "1": "abc",
# "2": "def",
# "3": "ghi",
# "4": "jkl",
# "5": "mno",
# "6": "pqrs",
# "7": "tuv",
# "8": "wxy",
# "9": "z"
# }

# from itertools import product

# string_maps = {
#     "1": "abc",
#     "2": "def",
#     "3": "ghi",
#     "4": "jkl",
#     "5": "mno",
#     "6": "pqrs",
#     "7": "tuv",
#     "8": "wxy",
#     "9": "z"
# }


# def get_two_letter_combinations(digits):
#     if len(digits) < 2:
#         print("Input must contain at least two digits.")
#         return[]
    
#     combinations = []

#     for i in range(len(digits)):
#         for j in range(i + 1, len(digits)):
#             first_letters = string_maps.get(digits[i], '')
#             second_letters = string_maps.get(digits[j], '')

#             if first_letters and second_letters:
#                 # Cartesian product of two letter groups
#                 for combo in product(first_letters, second_letters):
#                     combinations.append(''.join(combo))

#     return combinations

# digit_input = "123"
# result = get_two_letter_combinations(digit_input)
# print("Two-letter combinations:")
# for combo in result:
#     print(combo)


#               --------------------------------------------------------------------


# Write a Python program to add two positive integers without using the '+' operator.
# Note: Use bit wise operations to add two numbers.


# def add_without_plus(a, b):
#     while b != 0:

#         sum_without_carry = a ^ b

#         carry = (a & b) << 1

#         a = sum_without_carry
#         b = carry

#     return a

# num1 = 10 
# num2 = 4
# result = add_without_plus(num1, num2)

# print(f"The sum of {num1} and {num2} is: {result}")


#           ----------------------------------------------------------------

# Write a Python program to check the priority of the four operators (+, -, *, /).


# def check_operator_precedence():
#     print("Checking precedence between +, -, *, / operators in Python:\n")

#     expr1 = 2 + 3 * 4
#     print("Expression: 2 + 3 * 4")
#     print("Result:", expr1)
#     print("Explanation: '*' has higher precedence than '+', so it's evaluated as 2 + (3 * 4) = 14\n")

#     expr2 = (2 + 3) * 4
#     print("Expression: (2 + 3) * 4")
#     print("Result:", expr2)
#     print("Explanation: Parentheses force '+' to be evaluated first, so it's (5) * 4 = 20\n")

#     expr3 = 10 - 6 / 2
#     print("Expression: 10 - 6 / 2")
#     print("Result:", expr3)
#     print("Explanation: '/' has higher precedence than '-', so it's evaluated as 10 - (6 / 2) = 7.0\n")

#     expr4 = 10 / 2 * 3
#     print("Expression: 10 / 2 * 3")
#     print("Result:", expr4)
#     print("Explanation: '*' and '/' have same precedence and are evaluated left to right → (10 / 2) * 3 = 15.0\n")

# check_operator_precedence()


