

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

# List of Tuples: Create a list of tuples, where each tuple contains a name and an age, e.g., [('Alice', 30), ('Bob', 25)]. Print the name of the second person.

# people = [('Alice', 30), ('Bob', 25)]

# second_person = people[1]

# print("The name of the second person is:", second_person[0])

#                         --------------------------------------------------------------------

# Find Second Largest: Write a program to find the second largest number in a list.

# def f_second_largest(numbers):
#     unique_numbers = list(set(numbers))
#     unique_numbers.sort(reverse=True)
    
#     if len(unique_numbers) < 2:
#         return None  
    
#     return unique_numbers[1]

# numbers = [10, 20, 30, 40, 50, 60]
# second_largest = f_second_largest(numbers)
# print("Second largest number:", second_largest)


#                         --------------------------------------------------------------------

# Rotate List: Write a function that takes a list and an integer k, then rotates the list to the right by k steps. For example, [1, 2, 3, 4, 5] with k=2 becomes [4, 5, 1, 2, 3].

# def rotate_list(lst, k):
#     k = k % len(lst)  
#     return lst[-k:] + lst[:-k]

# my_list = [1, 2, 3, 4, 5]
# k = 2
# rotated_list = rotate_list(my_list, k)
# print("Rotated List:", rotated_list)

#                         --------------------------------------------------------------------

# Flatten a Nested List: Given a nested list like [[1, 2, [3]], 4, 5], write a program to flatten it into a single list [1, 2, 3, 4, 5].

# def flatten_list(nested_list):
#     flattened = []
    
#     for item in nested_list:
#         if isinstance(item, list):
#             flattened.extend(flatten_list(item))  # Recursively flatten sublists
#         else:
#             flattened.append(item)
    
#     return flattened

# nested_list = [[1, 2, [3]], 4, 5]
# flattened = flatten_list(nested_list)
# print("Flattened List:", flattened)


#                         --------------------------------------------------------------------

# Pascal's Triangle: Generate the first n rows of Pascal's triangle and store them as a nested list.

# def generate_pascals_triangle(n):
#     triangle = []
    
#     for row_num in range(n):
#         row = [1] * (row_num + 1)  
        
#         for j in range(1, row_num):
#             row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        
#         triangle.append(row)
    
#     return triangle

# n = 10
# pascals_triangle = generate_pascals_triangle(n)
# for row in pascals_triangle:
#     print(row)


#                         --------------------------------------------------------------------

# List Comprehension with If-Else: Create a list using list comprehension that contains "Even" or "Odd" for each number in a list of integers.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_odd = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
# print(even_odd)

#                         --------------------------------------------------------------------

# Sublist Search: Given two lists, list_A and list_B, check if list_B is a sublist of list_A.

# list_A = [10, 20, 30, 40, 50, 60]
# list_B = [30, 40, 50]

# is_sublist = any(list_A[i:i+len(list_B)] == list_B for i in range(len(list_A) - len(list_B) + 1))
# print(f"Is list_B a sublist of list_A? {is_sublist}")


#                         --------------------------------------------------------------------

# Sudoku Checker: Given a 9x9 grid represented as a nested list, write a function that checks if it is a valid Sudoku board (without checking the 3x3 squares).

# def is_valid_sudoku(board):
#     for row in board:
#         if len(set(row)) != 9:
#             return False
    
#     for col in range(9):
#         column = [board[row][col] for row in range(9)]
#         if len(set(column)) != 9:
#             return False
    
#     return True

# sudoku_grid = [
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ]

# print(is_valid_sudoku(sudoku_grid))  


#                         --------------------------------------------------------------------

# Prime Numbers: Create a program that generates a list of prime numbers up to a given limit using a list and loops.

# def generate_primes(limit):
#     primes = []
#     for num in range(2, limit + 1):
#         is_prime = True
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#     return primes

# prime_numbers = generate_primes(50)
# print(prime_numbers)

#                         --------------------------------------------------------------------

# Fibonacci Sequence: Generate the first n numbers of the Fibonacci sequence and store them in a list.

# def fibonacci(n):
#     fib_sequence = []
#     a, b = 0, 1
#     for _ in range(n):
#         fib_sequence.append(a)
#         a, b = b, a + b
#     return fib_sequence

# n = 10
# fib_list = fibonacci(n)
# print(fib_list)


#                         --------------------------------------------------------------------

# Sieve of Eratosthenes: Implement the Sieve of Eratosthenes algorithm to find all prime numbers up to a specified integer.

# def sieve_of_eratosthenes(limit):
#     primes = [True] * (limit + 1)
#     primes[0], primes[1] = False, False  
#     for i in range(2, int(limit ** 0.5) + 1):
#         if primes[i]:
#             for j in range(i * i, limit + 1, i):
#                 primes[j] = False
#     return [x for x in range(2, limit + 1) if primes[x]]

# limit = 50
# prime_numbers = sieve_of_eratosthenes(limit)
# print(prime_numbers)



#                         --------------------------------------------------------------------


# Matrix Transpose: Given a matrix represented by a nested list, create a new list that is the transpose of the original.


# def transpose_matrix(matrix):
#     return [list(row) for row in zip(*matrix)]

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# transposed = transpose_matrix(matrix)
# print(transposed)


#                         --------------------------------------------------------------------

# Anagrams: Given a list of words, group them into anagrams (e.g., ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'] becomes [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]).

# from collections import defaultdict

# def group_anagrams(words):
#     anagrams = defaultdict(list)
#     for word in words:
#         sorted_word = ''.join(sorted(word))
#         anagrams[sorted_word].append(word)
#     return list(anagrams.values())

# words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# anagram_groups = group_anagrams(words)
# print(anagram_groups)


#                         --------------------------------------------------------------------

# Most Frequent Element: Find the element that appears most frequently in a list.


# from collections import Counter

# elements = [1, 3, 2, 3, 3, 5, 6, 2, 3]

# counter = Counter(elements)

# most_frequent = counter.most_common(1)[0]

# print(f"The most frequent element is {most_frequent[0]} with {most_frequent[1]} occurrences.")


#                         --------------------------------------------------------------------

# Merge Sorted Lists: Given two sorted lists, merge them into a single sorted list. You cannot use the built-in sort() method on the final list.

# def merge_sorted_lists(list1, list2):
#     merged_list = []
#     i, j = 0, 0

#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             merged_list.append(list1[i])
#             i += 1
#         else:
#             merged_list.append(list2[j])
#             j += 1

#     merged_list.extend(list1[i:])
#     merged_list.extend(list2[j:])
    
#     return merged_list

# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8]

# merged = merge_sorted_lists(list1, list2)
# print("Merged list:", merged)


#                         --------------------------------------------------------------------

# Longest Common Subsequence: Find the length of the longest common subsequence between two lists.

# def longest_common_subsequence(list1, list2):
#     m, n = len(list1), len(list2)
#     dp = [[0] * (n + 1) for _ in range(m + 1)]

#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if list1[i - 1] == list2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

#     return dp[m][n]

# list1 = [1, 2, 3, 4, 1]
# list2 = [3, 4, 1, 2, 1]

# lcs_length = longest_common_subsequence(list1, list2)
# print("Length of the longest common subsequence:", lcs_length)


#                         --------------------------------------------------------------------

# Wave Array: Given an array, sort it into a "wave" form. An array arr[0...n-1] is sorted in wave form if arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4]...


# def wave_array(arr): 
#     arr.sort()
 
#     for i in range(0, len(arr) - 1, 2):
#         arr[i], arr[i + 1] = arr[i + 1], arr[i]

#     return arr

# arr = [1, 2, 3, 4, 5, 6]

# wave_arr = wave_array(arr)
# print("Wave array:", wave_arr)


#                         --------------------------------------------------------------------

# List Intersection: Find the intersection of two lists (all elements that are in both lists).

# def list_intersection(list1, list2):
#     return list(set(list1) & set(list2))

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7]
# intersection = list_intersection(list1, list2)
# print("Intersection of the lists:", intersection)



#                         --------------------------------------------------------------------

# List Union: Find the union of two lists (all unique elements from both lists).


# def list_union(list1, list2):
#     return list(set(list1) | set(list2))

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7]
# union = list_union(list1, list2)
# print("Union of the lists:", union)


#                         --------------------------------------------------------------------

# Cartesian Product: Given two lists, find their Cartesian product (a list of all possible pairs of elements from both lists).


# from itertools import product

# def cartesian_product(list1, list2):
#     return list(product(list1, list2))

# list1 = [1, 2, 3]
# list2 = ['a', 'b']
# result = cartesian_product(list1, list2)
# print("Cartesian Product:", result)


#                         --------------------------------------------------------------------

# Spiral Matrix: Given a matrix (nested list), print all elements of the matrix in spiral order.

# def spiral_matrix(matrix):
#     result = []
#     while matrix:
#         # Add the first row
#         result += matrix.pop(0)
        
#         # Add the last element of each remaining row
#         if matrix and matrix[0]:
#             for row in matrix:
#                 result.append(row.pop())
        
#         # Add the last row in reverse order
#         if matrix:
#             result += matrix.pop()[::-1]
        
#         # Add the first element of each remaining row (in reverse)
#         if matrix and matrix[0]:
#             for row in matrix[::-1]:
#                 result.append(row.pop(0))

#     return result

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]

# result = spiral_matrix(matrix)
# print("Spiral Order:", result)


#                         --------------------------------------------------------------------

# Remove Nth Node from End: Given a list, remove the nth element from the end of the list.

# def remove_nth_from_end(lst, n):
#     index_to_remove = len(lst) - n
#     if index_to_remove >= 0:
#         lst.pop(index_to_remove)
#     return lst

# numbers = [1, 2, 3, 4, 5]
# n = 4  
# print(remove_nth_from_end(numbers, n))


#                         --------------------------------------------------------------------

# Kadane's Algorithm: Given a list of numbers, find the contiguous sub-array with the largest sum.

# def kadane_algorithm(nums):
#     max_sum = current_sum = nums[0]
    
#     for num in nums[1:]:
#         current_sum = max(num, current_sum + num)  
#         max_sum = max(max_sum, current_sum)  
#     return max_sum

# numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(kadane_algorithm(numbers))


#                         --------------------------------------------------------------------

# Counting Inversions: In a list of numbers, an inversion is a pair of indices i, j such that i < j and a[i] > a[j]. Count the number of inversions.

# def count_inversions(arr):
#     count = 0
#     n = len(arr)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if arr[i] > arr[j]:
#                 count += 1
#     return count

# numbers = [5, 4, 9, 3, 7]
# inversions = count_inversions(numbers)
# print(f"Number of inversions: {inversions}")


#                         --------------------------------------------------------------------

# Permutations: Given a list of distinct numbers, return all possible permutations.

# import itertools

# def get_permutations(nums):
#     return list(itertools.permutations(nums))

# nums = [1, 2, 3]
# permutations = get_permutations(nums)
# print(f"All permutations: {permutations}")


#                         --------------------------------------------------------------------

# Combination Sum: Given a list of distinct integers and a target integer, return a list of all unique combinations where the chosen numbers sum to the target.

# def combination_sum(candidates, target):
#     def backtrack(start, target, path):
#         if target == 0:
#             result.append(list(path))
#             return
#         if target < 0:
#             return
#         for i in range(start, len(candidates)):
#             path.append(candidates[i])
#             backtrack(i, target - candidates[i], path)  
#             path.pop()  
    
#     result = []
#     candidates.sort()  
#     backtrack(0, target, [])
#     return result

# candidates = [2, 3, 6, 7]
# target = 7
# combinations = combination_sum(candidates, target)
# print(f"Unique combinations: {combinations}")


#                         --------------------------------------------------------------------
