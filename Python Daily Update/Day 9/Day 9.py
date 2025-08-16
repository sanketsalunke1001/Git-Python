
# Create a set of 5 fruits and print it.

# fruits = {"apple", "banana", "cherry", "orange", "grape"}

# print(fruits)

#                         --------------------------------------------------------------------

# Create a set of numbers and show that duplicates are automatically removed.

# numbers = {1, 2, 2, 3, 4, 4, 5}

# print("Set of numbers (duplicates removed):", numbers)

#                         --------------------------------------------------------------------

# Create an empty set and add 5 city names to it.

# cities = set()

# cities.add("Mumbai")
# cities.add("Pune")
# cities.add("Hydrabad")
# cities.add("Bangalore")
# cities.add("Delhi")

# print("Set of cities:", cities)

#                         --------------------------------------------------------------------

# Add two new colors to a set called colors.

# colors = {"red", "blue", "green"}

# colors.add("yellow")
# colors.add("purple")

# print("Set of colors:", colors)  # Randomly adding in set unorganized


#                         --------------------------------------------------------------------

# Remove a fruit from a set using remove() method.

# fruits = {"apple", "banana", "cherry", "orange"}

# fruits.remove("orange")

# print(fruits)

#                         --------------------------------------------------------------------

# Remove an animal from a set using discard() method (animal might not exist).


# animals = {"cat", "dog", "elephant", "tiger"}
# animals.discard("tiger")   # Can be removed due to presense in set
# animals.discard("lion")  # Lion not exist, won't raise an error
# print(animals)

#                         --------------------------------------------------------------------

# Use pop() on a set and print the removed element.

# fruits = {"apple", "banana", "cherry", "orange"}
# removed_item = fruits.pop()  
# print(f"Removed item: {removed_item}")
# print(fruits)


#                         --------------------------------------------------------------------

# Clear all items from a set and print it.

# animals = {"cat", "dog", "elephant", "tiger"}
# animals.clear()
# print(animals)

#                         --------------------------------------------------------------------

# Create a set of subjects and check if "Math" is present in it.

# subjects = {"English", "Math", "Science", "History", "Art"}

# is_math_present = "Math" in subjects

# print(is_math_present)

#                         --------------------------------------------------------------------

# Find the length of a set containing different countries.

# countries = {"India", "USA", "Dubai", "Germany", "France"}

# countries_length = len(countries)

# print(countries_length)

#                         --------------------------------------------------------------------

# Create two sets of numbers and find their union.

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# # #     union_set = set1 | set2  

# union_set =set1.union(set2)

# print(union_set)


#                         --------------------------------------------------------------------

# Create two sets of numbers and find their intersection.

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# #   #   intersection_set = set1 & set2 

# intersection_set = set1.intersection(set2)

# print(intersection_set)

#                         --------------------------------------------------------------------

# Create two sets of names and find the difference between them.

# set1 = {"Sanket", "Salunke", "Dharashiv", "27"}
# set2 = {"Sanket", "Salunke", "18"}

# difference = set1 - set2

# print("Difference between set1 and set2:", difference)


#                         --------------------------------------------------------------------

# Create two sets of numbers and find the symmetric difference.

# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}

# symmetric_difference = set_a ^ set_b
# print("Symmetric difference between set_a and set_b:", symmetric_difference)


#                         --------------------------------------------------------------------

# Create two sets: odd_numbers and even_numbers. Find their union.


# odd_numbers = {1, 3, 5, 7, 9}
# even_numbers = {2, 4, 6, 8, 10}

# #   # union = odd_numbers | even_numbers

# union = odd_numbers.union(even_numbers)

# print("Union of odd_numbers and even_numbers:", union)


#                         --------------------------------------------------------------------

# Create two sets of sports and check if they have any common sport.


# sports_set1 = {"Soccer", "Basketball", "Tennis"}
# sports_set2 = {"Tennis", "Cricket", "Baseball"}

# #       # common_sports = sports_set1 & sports_set2

# common_sports = sports_set1.intersection(sports_set2)

# if common_sports:
#     print("Common sports:", common_sports)
# else:
#     print("No common sports.")


#                         --------------------------------------------------------------------

# Given A = {1, 2, 3} and B = {1, 2, 3, 4, 5}, check if A is a subset of B.

# A = {1, 2, 3}
# B = {1, 2, 3, 4, 5}

# is_subset = A.issubset(B)
# print("Is A a subset of B?", is_subset)


#                         --------------------------------------------------------------------

# Given X = {2, 4, 6, 8} and Y = {4, 8}, check if Y is a subset of X.

# X = {2, 4, 6, 8}
# Y = {4, 8}

# is_subset = Y.issubset(X)
# print("Is Y a subset of X?", is_subset)


#                         --------------------------------------------------------------------

# Find if two sets are disjoint (no common elements).

# set1 = {1, 2, 3}
# set2 = {4, 5, 6}

# disjoint = set1.isdisjoint(set2)
# print("Are the sets disjoint?", disjoint)


#                         --------------------------------------------------------------------

# Create two sets and update the first one with the union of both.

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# set1.update(set2)

# print("Updated set1 with union of set1 and set2:", set1)


#                         --------------------------------------------------------------------

# Loop through a set of animals and print each one.

# animals = {"cat", "dog", "elephant", "tiger"}
# for animal in animals:
#     print(animal)

#                         --------------------------------------------------------------------

# Count how many elements in a set are greater than 50.

# numbers = {10, 25, 50, 75, 100, 30, 45}
# count = sum(1 for num in numbers if num > 50)
# print(f"Count of elements greater than 50: {count}")


#                         --------------------------------------------------------------------

# From a set of words, print only those words which have more than 5 letters.

# words = {"apple", "banana", "cherry", "kiwi", "grape"}
# for word in words:
#     if len(word) > 5:
#         print(word)

#                         --------------------------------------------------------------------

# Merge two sets using a loop (without using union method).

# set1 = {1, 2, 3, 4}
# set2 = {5, 6, 7, 8}
# new_set = set1.copy()  
# for item in set2:
#     new_set.add(item)  
# print(new_set)


#                         --------------------------------------------------------------------

# From a set of marks, print only marks greater than or equal to 90.

# marks = {85, 90, 95, 88, 76, 92}

# high_marks = {mark for mark in marks if mark >= 90}
# print("Marks greater than or equal to 90:", high_marks)


#                         --------------------------------------------------------------------

# Find common elements between two sets without using intersection method.

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# common_elements = {elem for elem in set1 if elem in set2}
# print("Common elements between the two sets:", common_elements)


#                         --------------------------------------------------------------------

# Print the largest number from a set of integers.


# numbers = {10, 20, 35, 50, 45}

# largest_number = max(numbers)
# print("Largest number:", largest_number)

#                         --------------------------------------------------------------------

# Print the smallest number from a set of integers.

# numbers = {10, 20, 35, 50, 45}

# smallest_number = min(numbers)
# print("Smallest number:", smallest_number)

#                         --------------------------------------------------------------------

# From a set of strings, find the longest string.

# strings = {"Sanket", "Salunke", "sjfbdkfbkdsb", "knfkdn"}
# longest_string = max(strings, key=len)
# print(f"The longest string is: {longest_string}")


#                         --------------------------------------------------------------------

# From a set of strings, find the shortest string.


# strings = {"Sanket", "Salunke", "sjfbdkfbkdsb", "knfkdn"}
# longest_string = min(strings, key=len)
# print(f"The longest string is: {longest_string}")


#                         --------------------------------------------------------------------

# Convert a list of numbers with duplicates into a set (remove duplicates).

# numbers = [1, 1, 2, 3, 3, 2, 4, 3, 5]
# unique_numbers = set(numbers)
# print(f"Unique numbers: {unique_numbers}")

#                         --------------------------------------------------------------------

# Convert a tuple of fruits into a set.

# fruits_tuple = ("apple", "banana", "cherry", "apple")
# fruits_set = set(fruits_tuple)
# print(f"Fruits set: {fruits_set}")

#                         --------------------------------------------------------------------

