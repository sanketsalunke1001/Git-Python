

# Create a list of your 5 favorite fruits and print the list.

# Favorite_fruits = ["Apple", "Grapes", "Mango", "Strawberry", "Blueberry"]

# print(Favorite_fruits)


#           -----------------------------------------------------------

# Print the third fruit from your list.

# Favorite_fruits = ["Apple", "Grapes", "Mango", "Strawberry", "Blueberry"]

# print(Favorite_fruits[2])

#           -----------------------------------------------------------

# Print the last fruit from your list using a negative index.

# Favorite_fruits = ["Apple", "Grapes", "Mango", "Strawberry", "Blueberry"]

# print(Favorite_fruits[-1])

#           -----------------------------------------------------------

# Change the second fruit in your list to "grape" and print the updated list.


# Favorite_fruits = ["Apple", "Grapes", "Mango", "Strawberry", "Blueberry"]

# Favorite_fruits[1] = "Grape"


# print(Favorite_fruits)



#                 -------------------------------------------------------------

# Add a new fruit "mango" to the end of your list.

# Favorite_fruits = ["Apple", "Grapes", "Mango", "Strawberry", "Blueberry"]

# Favorite_fruits.append("mango")  

# print(Favorite_fruits)

#                 -------------------------------------------------------------

# Insert "kiwi" at the beginning of your list.

# Favorite_fruits = ["Apple", "Grapes", "Mango", "Strawberry", "Blueberry"]

# Favorite_fruits.insert(0, "kiwi")

# print(Favorite_fruits)

#                 -------------------------------------------------------------

# Print the fruits from the second to the fourth position.


# Favorite_fruits = ["Apple", "Grapes", "Mango", "Strawberry", "Blueberry"]

# print(Favorite_fruits[1:4])

#                 -------------------------------------------------------------


# Print all fruits from the third position to the end.

# Favorite_fruits = ["Apple", "Grapes", "Mango", "Strawberry", "Blueberry"]

# print(Favorite_fruits[2:])

#                 -------------------------------------------------------------

# Print the number of fruits in your list.


# Favorite_fruits = ["Apple", "Grapes", "Mango", "Strawberry", "Blueberry"]

# print(len(Favorite_fruits))

#           --------------------------------------------------------------------

# Check if "apple" is in your list and print the result (True or False).


# Favorite_fruits = ["Apple", "Grapes", "Mango", "Strawberry", "Blueberry"]

# print("Apple" in Favorite_fruits)

#           --------------------------------------------------------------------

# List Methods
# Create a list of numbers: [10, 20, 30, 40, 50]. Use append() to add 60.

# numbers = [10, 20, 30, 40, 50]

# numbers.append(60)

# print(numbers)

#                       --------------------------------------------------------------------


# Use insert() to add 25 at index 2 of the number list.

# numbers = [10, 15, 20, 30, 35]
# numbers.insert(2, 25)  
# print(numbers)

#                       --------------------------------------------------------------------

# Use remove() to remove 40 from the number list.

# numbers = [10, 20, 30, 40, 50]
# numbers.remove(40)
# print(numbers)

#                       --------------------------------------------------------------------

# Use pop() to remove the last number from the list and print the removed number.

# numbers = [10, 20, 30, 40, 50, 60]

# removed_number = numbers.pop()

# print(removed_number)

#                       --------------------------------------------------------------------

# Use clear() to empty the list.

# numbers = [10, 15, 25, 20, 30, 35]
# numbers.clear()  
# print(numbers)

#                       --------------------------------------------------------------------

# Create a new list [1, 5, 2, 8, 3]. Use sort() to sort it in ascending order.


# numbers = [1, 5, 2, 8, 3]
# numbers.sort()
# print(numbers)

#                       --------------------------------------------------------------------

# Sort the list from the previous question in descending order.

# numbers = [10, 20, 30, 40, 50]

# numbers.sort(reverse=True)

# print(numbers)

#                       --------------------------------------------------------------------

# Create a list of strings: ["A", "C", "B"]. Sort it alphabetically.

# letters = ["A", "C", "B"]
# letters.sort()  
# print(letters)

#                       --------------------------------------------------------------------

# Create a list: ["red", "green", "blue"]. Use reverse() to reverse the order.


# colors = ["red", "green", "blue"]
# colors.reverse()
# print(colors)

#                       --------------------------------------------------------------------

# Create a list with duplicates: [1, 2, 2, 3, 4, 2]. Use count() to find how many times 2 appears.


# numbers = [1, 2, 2, 3, 4, 2]
# count_two = numbers.count(2)
# print(count_two)

#                       --------------------------------------------------------------------

# Combining Lists
# Create two lists: list_a = [1, 2] and list_b = [3, 4]. Combine them using + and store in list_c.

# list_a = [1, 2]
# list_b = [3, 4]

# list_c = list_a + list_b

# print(list_c)

#           ---------------------------------------------------------------------------

# Create two lists: list_d = ["a", "b"] and list_e = ["c", "d"]. Use extend() to add list_e to list_d.

# list_d = ["a", "b"]
# list_e = ["c", "d"]

# list_d.extend(list_e)

# print(list_d)

#           ---------------------------------------------------------------------------

# What's the difference between append() and extend()? Give an example.


# list1 = [10, 20, 30]
# list1.append([40, 50])
# print("After append:", list1)

# list2 = [10, 20, 30]
# list3 = [33, 44, 55]

# list2.extend([40, 50])

# list3.extend(list2)
# print("After extend:", list2)
# print(list3)

#                           ----------------------------------------------------------------------

# Create a list my_list = [1, 2, 3] and assign new_list = my_list. Modify new_list by adding 4. What does my_list look like? Why?


# my_list = [1, 2, 3]
# new_list = my_list

# my_list.append(4)

# print(my_list)
# print(new_list)

#                           ----------------------------------------------------------------------

# Create a true copy of my_list from the previous question using copy(). Modify the copy and observe the original.


# my_list = [1, 2, 3, 4]

# copied_list = my_list.copy()

# copied_list.append(5)

# print("my_list:", my_list)
# print("copied_list:", copied_list)

#                           --------------------------------------------------------------------

# Loops & List Comprehension
# Use a for loop to print each item in a list of colors.

# colors = ["red", "green", "blue", "yellow"]

# for color in colors:
#     print(color)

#                           --------------------------------------------------------------------


# Use a for loop to print the square of each number in [1, 2, 3, 4].


# number = [1, 2, 3, 4]

# for num in number:
#     print(num ** 2)

#                           --------------------------------------------------------------------

# Use a for loop to find the largest number in a list of numbers.


# numbers = [15, 35, 22, 99, 66, 77, 555, 23]

# largest = numbers[0]

# for number in numbers:
#     if number > largest:
#         largest = number

# print("The largest number is:", largest)

#                           --------------------------------------------------------------------


# Create a new list using list comprehension that contains only the even numbers from [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

# numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_numbers = [num for num in numbers if num % 2 == 0]

# print(even_numbers)

#                           --------------------------------------------------------------------

# Vowel Counter: Create a list of vowels ['a', 'e', 'i', 'o', 'u']. Ask the user to input a word,
#  then use a loop to count how many vowels are in the word.


# vowels = ['a', 'e', 'i', 'o', 'u']
# word = input("Enter a word: ").lower()  # Convert to lowercase to match vowel list
# count = 0

# for letter in word:
#     if letter in vowels:
#         count = count + 1

# print("Number of vowels:", count)
 
#                         --------------------------------------------------------------------

# Reverse a String: Take a string (e.g., "Python") and use a list to reverse it.

# text = "Python"

# char_list = list(text)

# char_list.reverse()

# reversed_text = ''.join(char_list)

# print("Reversed string:", reversed_text)


#                         --------------------------------------------------------------------


# Sum of a List: Write a program that calculates the sum of all numbers in a list.

# numbers = [10, 2, 30, 40, 50]

# total = sum(numbers)

# print("Sum of the list is:", total)

#                         --------------------------------------------------------------------


# Find the Smallest Number: Write a program to find the smallest number in a list without using the min() function.


# def find_smallest_number(numbers):
#     if not numbers:
#         return None  
    
#     smallest = numbers[0]
#     for num in numbers:
#         if num < smallest:
#             smallest = num
#     return smallest

# list = [55, 34, 44, 23, 0, 64, -33]
# result = find_smallest_number(list)
# print("The smallest number is:", result)

#                         --------------------------------------------------------------------

# Remove Duplicates: Given a list with duplicate numbers, create a new list that contains only the unique numbers.

# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique_num = list(set(numbers))
# print(unique_num)

#                         --------------------------------------------------------------------

# Tic-Tac-Toe Board: Create a list that represents a simple Tic-Tac-Toe board [['', '', ''], ['', '', ''], ['', '', '']]. Print the board.

# board = [['', '', ''],
#          ['', '', ''],
#          ['', '', '']]

# for row in board:
#     print(row)

#                         --------------------------------------------------------------------

# Guess the Number Game: Create a list of 5 numbers. Ask the user to guess a number. Check if the guessed number is in the list and tell them if they are correct.

# import random

# number_list = random.sample(range(1, 21), 5)

# guess = int(input("Guess a number between 1 and 20: "))

# if guess in number_list:
#     print("Correct! 🎉 Your guess is in the list.")
# else:
#     print("Sorry, that's not in the list.")

# print("The list was:", number_list)

#                         --------------------------------------------------------------------


# Split a Sentence: Take a sentence from the user and use the split() method to create a list of words. Print the list.

# sentence = input("Enter a sentence: ")

# words = sentence.split()

# print("List of words:", words)

#                         --------------------------------------------------------------------


# Join a List: Take a list of words and use the join() method to turn it back into a single sentence.


# words = ["S", "A", "N", "K","E","T"]
# sentence = " ".join(words)
# print(sentence)

#                         --------------------------------------------------------------------

# Factorial: Create a list to store the factorial of a given number.

# n = 5

# factorials = []

# fact = 1
# for i in range(1, n + 1):
#     fact = fact * i
#     factorials.append(fact)

# print(factorials)

#                         --------------------------------------------------------------------

# Palindrome Checker: Take a word from the user and check if it's a palindrome (reads the same forwards and backwards)
#  by comparing the original list of characters with its reversed version.


# word = input("Enter a word: ")

# if word == word[::-1]:
#     print(f"'{word}' is a palindrome!")
# else:
#     print(f"'{word}' is not a palindrome.")

#                         --------------------------------------------------------------------

# Nested List: Create a list that contains two other lists (e.g., [[1, 2], [3, 4]]). Access and print the number 4.

# nested_list = [[1, 2], [3, 4]]
# print(nested_list[1][1])

#                         --------------------------------------------------------------------

# Matrix Addition: Add two matrices (represented as nested lists) of the same size.

# matrix1 = [[1, 2, 3],
#            [4, 5, 6],
#            [7, 8, 9]]

# matrix2 = [[9, 8, 7],
#            [6, 5, 4],
#            [3, 2, 1]]

# result = []

# for i in range(len(matrix1)):
#     row = []
#     for j in range(len(matrix1[i])):
#         row.append(matrix1[i][j] + matrix2[i][j])
#     result.append(row)

# for row in result:
#     print(row)

#                         --------------------------------------------------------------------


# Counting Words: Take a sentence and count how many times each word appears. Store the result in a list of lists (e.g., [['hello', 2], ['world', 1]]).

# def count_words(sentence):
#     words = sentence.lower().split()

#     word_count = {}

#     for word in words:
#         word_count[word] = word_count.get(word, 0) + 1

#     result = [[word, count] for word, count in word_count.items()]
    
#     return result

# sentence = input("Enter a sentence: ")

# word_count_result = count_words(sentence)
# print("Word counts:", word_count_result)

#                         --------------------------------------------------------------------

# Shopping List: Create an empty list called shopping_list. Ask the user to enter 3 items and add each to the list. Print the final list.


# shopping_list = []

# for i in range(3):
#     item = input(f"Enter item {i+1}: ")
#     shopping_list.append(item)

# print("Your shopping list:", shopping_list)

#                         --------------------------------------------------------------------

# Filter a List: Create a function that takes a list of numbers and a threshold value, then returns a new list containing only the numbers greater than the threshold.

# def filter_numbers(numbers, threshold):
#     return [num for num in numbers if num > threshold]

# numbers = [1, 5, 8, 2, 10, 3]
# threshold = 5
# filtered_numbers = filter_numbers(numbers, threshold)
# print(filtered_numbers)


#                         --------------------------------------------------------------------

# Slicing Challenge: Given data = ['A', 'B', 'C', 'D', 'E', 'F'], print a new list containing ['C', 'D'] using slicing.

# data = ['A', 'B', 'C', 'D', 'E', 'F']

# sublist = data[2:4]

# print(sublist) 

# # # print(data)

#                         --------------------------------------------------------------------

# index() with try-except: Use try-except to gracefully handle the error that occurs when index() is called on an item not in the list.


# def find_item_index(item, my_list):
#     try:
#         index = my_list.index(item)
#         return f"Item found at index {index}"
#     except ValueError:
#         return f"Error: {item} is not in the list."

# my_list = [1, 2, 3, 4, 5]

# item_to_find = input("Enter an item to find its index: ")

# if item_to_find.isdigit():
#     item_to_find = int(item_to_find)

# result = find_item_index(item_to_find, my_list)
# print(result)


#                         --------------------------------------------------------------------


# Removing Specific Items: Write a program that takes a list and a value, then removes all occurrences of that value from the list.


# def remove_occurance (lst, value):
#     while value in lst:
#         lst.remove(value)
#     return lst

# my_list = [10, 20, 30, 20, 40, 20]

# value_to_remove = int(input("Enter the value to remove: "))

# updated_list = remove_occurance(my_list, value_to_remove)
# print("Updated list:", updated_list)

#                         --------------------------------------------------------------------
