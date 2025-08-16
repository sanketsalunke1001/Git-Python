
# Create an empty tuple and print its type.

# empty_tuple = ()
# print("Type of empty_tuple:", type(empty_tuple))

#                         --------------------------------------------------------------------


# Create a tuple with numbers 1 to 5 and print it.

# numbers_tuple = (1, 2, 3, 4, 5)
# print("Tuple with numbers 1 to 5:", numbers_tuple)

#                         --------------------------------------------------------------------

# Create a tuple with different data types (integer, string, boolean, float).

# mixed_tuple = (10, "Hello", True, 3.14)
# print("Tuple with mixed data types:", mixed_tuple)

#                         --------------------------------------------------------------------

# Create a tuple without using parentheses and print it.

# tuple_without_parentheses = 1, 2, 3, 4, 5
# print("Tuple without parentheses:", tuple_without_parentheses)

#                         --------------------------------------------------------------------

# Create a tuple with a single element and show its type.

# single_element_tuple = (5)
# print(single_element_tuple)
# print(type(single_element_tuple))

#                         --------------------------------------------------------------------

# Create a tuple from a list [1, 2, 3] using the tuple() function.

# list_numbers = [1, 2, 3]
# tuple_from_list = tuple(list_numbers)
# print(tuple_from_list)

#                         --------------------------------------------------------------------

# Create a tuple from the string "Python" and print it.

# string = "Python"
# tuple_from_string = tuple(string)
# print(tuple_from_string)

#                         --------------------------------------------------------------------

# Access the 3rd element of a tuple (10, 20, 30, 40, 50).

# numbers_tuple = (10, 20, 30, 40, 50)
# third_element = numbers_tuple[2]  
# print(third_element)

#                         --------------------------------------------------------------------

# Access the last element of a tuple (5, 10, 15, 20).

# tuple = (5, 10, 15, 20)

# last_element = tuple[-1]

# print(last_element)

#                         --------------------------------------------------------------------


# Create a tuple (1, 2, 3, 1, 4, 1) and count how many times 1 appears.

# my_tuple = (1, 2, 3, 1, 4, 1)

# count_one = my_tuple.count(1)

# print(count_one)

#                         --------------------------------------------------------------------


# Find the index of 50 in (10, 20, 30, 40, 50).

# my_tuple = (10, 20, 30, 40, 50)

# index_50 = my_tuple.index(50)

# print(index_50)

#                         --------------------------------------------------------------------

# Try to modify a tuple (1, 2, 3) by changing its first element. What happens?

# my_tuple = (1, 2, 3)

# try:
#     my_tuple[0] = 10  
# except TypeError as e:
#     print(e)

#                         --------------------------------------------------------------------

# Swap the values of two variables using tuple unpacking.

# a = 5
# b = 10
# a, b = b, a  
# print("a:", a, "b:", b)

#                         --------------------------------------------------------------------

# Create a nested tuple ((1, 2), (3, 4)) and print the second element of the first tuple.

# nested_tuple = ((1, 2), (3, 4))

# print("Second element of the first tuple:", nested_tuple[0][1])


#                         --------------------------------------------------------------------

# Create a tuple (1, 2, 3) and convert it into a list.

# tuple_example = (1, 2, 3)

# list_from_tuple = list(tuple_example)
# print("List from tuple:", list_from_tuple)


#                         --------------------------------------------------------------------

# Iterate over (10, 20, 30, 40) and print each element.

# tuple = (10, 20, 30, 40)

# for item in tuple:
#     print(item)

#                         --------------------------------------------------------------------

# Iterate over (5, 10, 15) and print only even numbers.

# numbers = (5, 10, 15)
# for num in numbers:
#     if num % 2 == 0:
#         print(num)


#                         --------------------------------------------------------------------

# Find the length of (1, 2, 3, 4, 5).

# numbers = (1, 2, 3, 4, 5)
# length = len(numbers)
# print(length)


#                         --------------------------------------------------------------------

# Write a program to check if a tuple is empty.

# empty_tuple = ()
# if not empty_tuple:
#     print("The tuple is empty")
# else:
#     print("The tuple is not empty")


# empty_tuple1 = (1)
# if not empty_tuple1:
#     print("The tuple is empty")
# else:
#     print("The tuple is not empty")


#                         --------------------------------------------------------------------

# Reverse (10, 20, 30, 40) using slicing.

# numbers = (10, 20, 30, 40)
# reversed_numbers = numbers[::-1]
# print(reversed_numbers)

#                         --------------------------------------------------------------------

# create a tuple (1, 2, 3, 4, 5) and get elements at even indexes only.

# my_tuple = (1, 2, 3, 4, 5)

# even_index_elements = my_tuple[::2]         # Get elements at even indexes (0, 2, 4)

# print(even_index_elements)

#                         -------------------------------------------------------------------

# Create a tuple (10, 20, 30, 40, 50) and get elements from index 1 to 4.

# my_tuple = (10, 20, 30, 40, 50)

# slice_elements = my_tuple[1:5]              # Get elements from index 1 to 4 (index 4 is exclusive)

# print(slice_elements)

#                         --------------------------------------------------------------------

# Create a tuple (10, 20, 30) and check if all elements are greater than 5.

# tuple = (10, 20, 30)

# all_greater_than_5 = all(x > 5 for x in tuple)

# print(all_greater_than_5)

#                         --------------------------------------------------------------------

# Create a tuple (5, 10, 15, 20) and calculate the sum of all elements.

# my_tuple = (5, 10, 15, 20)

# total_sum = sum(my_tuple)

# print(total_sum)

#                         --------------------------------------------------------------------

# Create a tuple (1, 2, 3, 4) and print elements in reverse order using a loop.

# tuple = (1, 2, 3, 4)

# for i in reversed(tuple):
#     print(i)

#                         --------------------------------------------------------------------

# Store the coordinates (27.1751, 78.0421) in a tuple and print them in “Latitude: X, Longitude: Y” format.

# coordinates = (27.1751, 78.0421)

# print(f"Latitude: {coordinates[0]}, Longitude: {coordinates[1]}")

#                         --------------------------------------------------------------------

# Store RGB values for red, green, and blue in tuples and print them.

# red = (255, 0, 0)       # RGB for red
# green = (0, 255, 0)     # RGB for green
# blue = (0, 0, 255)      # RGB for blue

# print("Red RGB:", red)
# print("Green RGB:", green)
# print("Blue RGB:", blue)

#                         --------------------------------------------------------------------

# Create a tuple containing the names of the days of the week. Print only weekends.

# days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# print("Weekends:", days_of_week[5], days_of_week[6])

#                         --------------------------------------------------------------------

# Store student details (Name, Age, Grade) in a tuple and print them in a formatted way.

# student = ("Sanket", 26, "A")
# name, age, grade = student
# print(f"Student Name: {name}")
# print(f"Age: {age}")
# print(f"Grade: {grade}")

#                         --------------------------------------------------------------------

# Create a tuple containing multiple lists and modify one of the lists inside it.

# nested_tuple = ([1, 2], [3, 4], [5, 6])
# nested_tuple[0].append(3)                   # Modifying the first list in the tuple
# print(nested_tuple)

#                         --------------------------------------------------------------------

# Create a tuple (1, 2, 3) and another tuple (4, 5, 6) — merge them without using +.

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# merged_tuple = tuple(tuple1.__add__(tuple2))
# print(merged_tuple)

#                         --------------------------------------------------------------------

# Write a program to check if two tuples have any elements in common.

# tuple1 = (1, 2, 3, 4)
# tuple2 = (3, 5, 6, 7)
# common_elements = set(tuple1).intersection(tuple2)

# if common_elements:
#     print(f"Common elements: {common_elements}")
# else:
#     print("No common elements")

#                         --------------------------------------------------------------------

# Write a program to convert a tuple of strings into a single concatenated string.

# strings = ("S", "A", "N", "K", "E", "T")
# concatenated_string = "".join(strings)
# print(concatenated_string)


#                         --------------------------------------------------------------------

# Write a program to find the maximum and minimum value from (5, 8, 2, 9, 1).

# numbers = (5, 8, 2, 9, 1)
# max_value = max(numbers)
# min_value = min(numbers)
# print(f"Max value: {max_value}")
# print(f"Min value: {min_value}")


#                         --------------------------------------------------------------------

# Write a program to count how many strings in a tuple start with the letter “A”.

# strings = ("Apple", "Banana", "Avocado", "Cherry", "Apricot")
# count = sum(1 for word in strings if word.startswith("A"))
# print(f"Number of strings starting with 'A': {count}")

#                         --------------------------------------------------------------------
