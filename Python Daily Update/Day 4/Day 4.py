# Slicing Strings
# Extract the first 5 characters from the string "HelloWorld".

# text = "Sanket Salunke"
# first_five = text[:6]
# print(first_five)

# A = "Hello, World!"
# print(A[:9])

#        ----------------------------------------------------

#   Get every second character from "pythonprogramming".

# ABC = "pythonprogramming"   # ptopormig
# every_second = ABC[::2]
# print(every_second)

#  Reverse the string "DataEngineer".

# text = "DataEngineer"   # reenignEataD    reinaa
# reversed_text = text[::-1]  # reversed_text = text[::-2]
# print(reversed_text)

#           -------------------------------------------

#  Slice "machinelearning" to get "learn".

# text = "machinelearning"
# slice_learn = text[7:12]
# print(slice_learn)

# print(text[7:12])


#       ------------------------------------------------

#   replace()
#   Replace all occurrences of "apple" with "orange" in "apple apple banana".


# text = "apple  banana"  # text = "apple  banana"
# new_text = text.replace("apple", "orange")
# print(new_text)


#           ---------------------------------------------------

#  Replace only the first "is" with "was" in "This is easy, is it not?".

# text = "This is easy, is it not?"  # text = "apple  banana"
# new_text = text.replace("is", "was")
# print(new_text)


# # anaother method for modifying
# text = "This is easy, was it not?"
# modified_text = text.replace("is", "was", 0)
# print(modified_text)

# ----------------------------------------

# Convert "HELLO EVERYONE" to all lowercase.

# text = "Hello World"
# lowercase_text = text.lower()
# print(lowercase_text)

#           ----------------------------------------------------------------

# Concatenation
# Concatenate "Good" and "Morning" with a space in between.

# A = "Hello"
# B = "World"
# result = A + " " + B
# print(result)

#       ------------------------------------------------------

# Join three strings "Data", "Science", "Rocks" using +.

# str1 = "Data"
# str2 = "Science"
# str3 = "Rocks"

# result = str1 + str2 + str3
# print(result)


# A = "Data"
# B = "Science"
# C = "Rocks"

# result = A + B + C
# print(result)

# result = str1 + " " + str2 + " " + str3 # to add extra space
# print(result)

#           -------------------------------------------------------

# format()
# Use .format() to insert a name "Ashutosh" and age 28 into "My name is {} and I am {} years old.".

# name = "Ashutosh"
# age = 28

# Text = "My name is {} and I am {} years old.".format(name, age)
# print(Text)

# print("My name is {} and I am {} years old.".format(name, age)) 

#           ------------------------------------------------------------

# Format the float value 45.6789 to show only 2 decimal places.

# value = 45.6789
# formatted_value = "{:.2f}".format(value)  # {:.3f} for .3 decimal value as value definer
# print(formatted_value)

#           -------------------------------------------------------

#  capitalize()
#  Capitalize the first letter of "hello world".

# A = "hello world"
# String = A.capitalize()
# print(String)

# # text = "hello world"
# # capitalized_text = text.capitalize()
# # print(capitalized_text)

#       ------------------------------------------------------

# casefold()
# Compare two strings "Python" and "PYTHON" for equality using .casefold().

# A = "Python"
# B = "PYTHON"

# # A = "Python"
# # B = "PYTHONs"

# Text = A.casefold() == B.casefold()
# print(Text)

#       ------------------------------------------------------

# center()
# Center the word "Python" in a string of length 20 using * as the fill character.

# text = "Python"
# centered_text = text.center(20, '*')
# print(centered_text)

# # ---------------------------------------------------------------------

# # count()
# # Count the number of occurrences of "a" in "banana".

# text = "banana"
# count_a = text.count("a")
# print(count_a)


# -----------------------------------------------------------

#   Count how many times "the" appears in "The theater is near the theme park" (case-insensitive).

# text = "The theater is near the theme park"
# count_the = text.lower().count("the")
# print(count_the)

#       ------------------------------------------------------------

# endswith()
# Check if "programming.py" ends with ".py".

# filename = "programming.py"
# result = filename.endswith(".py")
# print(result)

#Remaining


# Check if "hello.txt" ends with ".doc".

# Sample_Text = "hello.txt"
# if Sample_Text.endswith(".doc"):
#     print("Yes, it ends with .doc")
# else:
#     print("No, it does not end with .doc")

#   ------------------------------------------------------


# Mixed
# Take the string "hello world":

# Convert it to uppercase,

# text = "hello world"
# uppercase_text = text.upper()
# print(uppercase_text)


# Replace "HELLO" with "HI",

# text = "hello world"
# uppercase_text = text.upper()
# replaced_text = uppercase_text.replace("HELLO", "HI")
# print(replaced_text)


# Slice the last 5 characters.

# text = "hello world"
# uppercase_text = text.upper()              # "HELLO WORLD"
# replaced_text = uppercase_text.replace("HELLO", "HI")  # "HI WORLD"
# sliced_text = replaced_text[-5:]           # Last 5 characters
# print(sliced_text)


