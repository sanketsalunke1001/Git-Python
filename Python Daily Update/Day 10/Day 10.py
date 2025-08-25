
# Create a dictionary of 3 fruits and their colors. Print it.

# fruits = {"Banana": "Yellow", "Grapes": "Green", "Apple": "Red", "Mango ": "Yellow"}

# print("Fruits and their colors:", fruits)


#                         --------------------------------------------------------------------

# Create a dictionary of 3 countries and their capitals. Print only the capitals.

# countries = {
#     "India": "Delhi",
#     "Japan": "Tokyo",
#     "USA": "New York"
# }
# print("Capitals:", list(countries.values()))


#                         --------------------------------------------------------------------

# Add a new country-capital pair to the dictionary.

# countries = {
#     "India": "Delhi",
#     "Japan": "Tokyo",
#     "USA": "New York"
# }

# countries["canada"] = "ottawa"

# print("Countries:", countries)

#                         --------------------------------------------------------------------

# Update the capital of an existing country.

# countries = {
#     "India": "Delhi",
#     "Japan": "Tokyo",
#     "USA": "New York"
# }

# countries["India"] = "Mumbai"

# print("Countries :", countries)

#                         --------------------------------------------------------------------

# Delete one country from the dictionary.

# countries = {
#     "India": "Delhi",
#     "Japan": "Tokyo",
#     "USA": "New York"
# }

# del countries["USA"]

# print("Countries:", countries)


#                         --------------------------------------------------------------------


# Print only the keys of a dictionary.

# countries = {
#     "India": "Delhi",
#     "Japan": "Tokyo",
#     "USA": "New York"
# }

# print("Countries:", countries.keys())

# #    #      Print only the values of a dictionary.

# print(countries.values())

#                         --------------------------------------------------------------------


# Check if "India" is present as a key in your dictionary.

# countries = {
#     "India": "Delhi",
#     "Japan": "Tokyo",
#     "USA": "New York"
# }

# if "India" in countries:
#     print("India is present.")
# else:
#     print("India is not present.")

#                         --------------------------------------------------------------------

# Create a dictionary of your 3 friends and their ages. Print the age of one friend.

# friends = {
#     "Sanket": 27,
#     "Saurabh": 29,
#     "Sandesh": 26
# }
# print("Age of Sanket:", friends["Sanket"])



#                         --------------------------------------------------------------------

# Create an empty dictionary and add 3 key-value pairs one by one.

# dict = {}
# dict["Name"] = "sanket"
# dict["age"] = 27
# dict["City"] = "Dharashiv"

# print(dict)

#                         --------------------------------------------------------------------

# Write a program to count how many times each letter appears in the word "banana".

# fruit = "banana"
# letter_count = {}

# for letter in fruit:
#     if letter in letter_count:
#         letter_count[letter] = letter_count[letter] + 1
#     else:
#         letter_count[letter] = 1

# print("Letter count in 'banana':", letter_count)


#                         --------------------------------------------------------------------

# Store 5 students’ names and their marks in a dictionary. Print the student who scored the highest marks.


# students = {
#     "Sanket": 80,
#     "Sandesh": 83,
#     "Ajay": 97,
#     "Akash": 87,
#     "Sushant": 77
# }


# top_student = max(students, key=students.get)
# print("Top student:", top_student, "with marks:", students[top_student])


#                         --------------------------------------------------------------------

# Merge two dictionaries
# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}

                #### #                         --------
# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}

# d1.update(d2)
# print(d1)

# merged = {**d1, **d2}
# print(merged)


#                         --------------------------------------------------------------------

# Write a program to check if a dictionary is empty or not.

# my_dict = {}

# if not my_dict:
#     print("The dictionary is empty.")
# else:
#     print("The dictionary is not empty.")


#                         --------------------------------------------------------------------

# Given a dictionary:
# numbers = {1: "One", 2: "Two", 3: "Three"}
# Print the word for number 2.

# numbers = {1: "One", 2: "Two", 3: "Three"}

# print(numbers[2])

#                         --------------------------------------------------------------------

#  Write a program to create a dictionary of squares (keys 1 to 5, values = squares).
#  Write a program to get the sum of all values in a dictionary.
#  Write a program to find the key with the maximum value in a dictionary.
#  Write a program to swap keys and values in a dictionary.
#  Write a program to check if two dictionaries are equal or not.

# squares = {x: x**2 for x in range(1, 6)}
# print("Dictionary of squares:", squares)

# # 2. Get the sum of all values in the dictionary.
# sum_values = sum(squares.values())
# print("Sum of all values:", sum_values)

# # 3. Find the key with the maximum value in the dictionary.
# max_key = max(squares, key=squares.get)
# print("Key with the maximum value:", max_key)

# # 4. Swap keys and values in the dictionary.
# swapped = {value: key for key, value in squares.items()}
# print("Swapped dictionary:", swapped)


# Write a program to check if two dictionaries are equal or not.

# dict1 = {"x": 1, "y": 2}
# dict2 = {"y": 2, "x": 1}
# if dict1 == dict2:
#     print("The dictionaries are equal.")
# else:
#     print("The dictionaries are not equal.")

#                         --------------------------------------------------------------------

# Create a nested dictionary of 3 employees with their name, age, and department. Print one employee’s department.

# employees = {
#     "student1": {"name": "Sanket", "age": 28, "department": "Automobile"},
#     "student2": {"name": "Ajay", "age": 29, "department": "Mechanical"},
#     "student3": {"name": "Manish", "age": 26, "department": "Computer"}
# }

# print("Ajay's Department:", employees["student2"]["department"])


#                         --------------------------------------------------------------------

# Create a dictionary library with book titles as keys and authors as values. Print all book titles.

# library = {
#     "1984": "George Orwell",
#     "To Kill a Mockingbird": "Harper Lee",
#     "The Great Gatsby": "F. Scott Fitzgerald",
#     "Pride and Prejudice": "Jane Austen"
# }

# print("Book Titles in Library:")
# for title in library.keys():
#     print("-", title)


#                         --------------------------------------------------------------------

# Store your family members and their favorite food in a dictionary. Print the favorite food of your mom.

# favorite_foods = {
#     "dad": "Mutton",
#     "mom": "Chicken",
#     "sister": "maggi",
#     "brother": "Poha"
# }

# # Print mom’s favorite food
# print("Mom's favorite food:", favorite_foods["dad"])


#                         --------------------------------------------------------------------

# Write a program to count the frequency of each word in a sentence.

# sentence = "My name is  a sanket salunke"
# words = sentence.split()
# frequency = {}

# for word in words:
#     frequency[word] = frequency.get(word, 0) + 1

# print("Word Frequency:")
# for word, count in frequency.items():
#     print(f"{word}: {count}")


#                         --------------------------------------------------------------------

# Given a student dictionary with marks, calculate the average marks.

# student_marks = {
#     "Sanket": 80,
#     "Ajay": 75,
#     "Manish": 77,
#     "Jai": 67
# }
# average = sum(student_marks.values()) / len(student_marks)
# print("Average marks:", average)


#                         --------------------------------------------------------------------

# Create a dictionary of 3 states and their cities (list of cities as values). Print all cities of one state.


# states = {
#     "Maharastra": ["Mumbai", "Pune", "Solapur"],
#     "UP": ["Pryagraj", "Mirzapur", "Siwan"],
#     "TS": ["Hydrabad", "Sikandarabd", "Humnabad"]
# }
# print("Cities in Maharastra:", states["Maharastra"]


#                         --------------------------------------------------------------------

# Create a dictionary of 3 movies and their release years. Print movies released after 2010.

# movies = {
#     "Breaking Bad": 2010,
#     "Better call saul": 2014,
#     "Iron Man": 2015
# }

# print("Movies released after 2010:")
# for movie, year in movies.items():
#     if year > 2010:
#         print(f"- {movie} ({year})")


#                         --------------------------------------------------------------------

# Write a program to remove all duplicate values from a dictionary.

# original_dict = {
#     "a": 1,
#     "b": 1,
#     "c": 2,
#     "d": 3,
#     "e": 5,
#     "f": 7
# }

# unique_dict = {}
# seen_values = set()
# for key, value in original_dict.items():
#     if value not in seen_values:
#         unique_dict[key] = value
#         seen_values.add(value)
# print("Dictionary after removing duplicate values:", unique_dict)


#                         --------------------------------------------------------------------

# Create a dictionary of fruits and prices. Print all fruits costing more than 50.

# fruits = {
#     "apple": 100,
#     "banana": 40,
#     "mango": 70,
#     "cherry": 80,
#     "orange": 50,
#     "grapes": 90
# }

# print("Fruits costing more than 50:")
# for fruit, price in fruits.items():
#     if price > 50:
#         print(f"{fruit} - ₹{price}")

#                         --------------------------------------------------------------------

# Create a dictionary of rooms and treasures. Let the user choose a room and print the treasure.


# rooms  = {
#     "kitchen": "a golden spoon",
#     "bedroom": "a diamond ring",
#     "attic": "a mysterious map",
#     "basement": "a box of ancient coins"
# }

# choice = input("Choose a room (kitchen, bedroom, attic, basement): ").lower()

# if choice in rooms:
#     print(f"In the {choice}, you found {rooms[choice]}!")
# else:
#     print("That room doesn't exist.")


#                         --------------------------------------------------------------------

# Build a dictionary of countries and capitals. Ask the user to type a country and print its capital.


# countries = {
#     "India": "New Delhi",
#     "France": "Paris",
#     "Japan": "Tokyo",
#     "Brazil": "Brasília",
#     "Canada": "Ottawa"
# }

# country = input("\nEnter a country to find its capital: ").title()

# capital = countries.get(country)
# if capital:
#     print(f"The capital of {country} is {capital}.")
# else:
#     print("Country not found in the dictionary.")


#                         --------------------------------------------------------------------

# Create a quiz dictionary with 3 questions and answers. Ask user to answer and give score.

# quiz = {
#     "What is the capital of India?": "New Delhi",
#     "What is 20 + 5?": "25",
#     "Name is S?": "Sanket"
# }

# score = 0

# print("Quiz Time!")
# for question, correct_answer in quiz.items():
#     user_answer = input(question + " ").strip()
#     if user_answer.lower() == correct_answer.lower():
#         print("Correct!")
#         score += 1
#     else:
#         print(f"Wrong. The correct answer is {correct_answer}.")

# print(f"\nYour final score is {score}/{len(quiz)}.")


#                         --------------------------------------------------------------------

# Store student roll numbers and names. Ask the user to enter a roll number → print the name.

# students = {
#     11: "Sanket",
#     12: "Ajay",
#     13: "Akash"
# }

# roll = int(input("Enter roll number: "))

# if roll in students:
#     print(f"Name: {students[roll]}")
# else:
#     print("Roll number not found.")



#                         --------------------------------------------------------------------

# Create a dictionary of English words and their Hindi meanings. Ask the user to translate a word.


# dictionary = {
#     "apple": "सेब",
#     "water": "पानी",
#     "book": "किताब",
#     "sun": "सूरज"
# }

# word = input("Enter an English word to translate: ").lower()

# if word in dictionary:
#     print(f"The Hindi meaning of '{word}' is: {dictionary[word]}")
# else:
#     print("Word not found in dictionary.")


#                         --------------------------------------------------------------------

# Treasure Hunt: Store treasures in dictionary keys (Red Room, Blue Room, etc.). Let user guess the correct room.

# treasures = {
#     "Red Room": False,
#     "Blue Room": True,     # Let's say the treasure is in the Blue Room
#     "Green Room": False,
#     "Yellow Room": False
# }

# guess = input("Guess the room (Red Room, Blue Room, Green Room, Yellow Room): ")

# if guess in treasures:
#     if treasures[guess]:
#         print("Congratulations! You found the treasure! 🏆")
#     else:
#         print("Sorry, no treasure here. Try again!")
# else:
#     print("That room doesn't exist!")

#                         --------------------------------------------------------------------

# Create a dictionary of usernames and passwords. Ask user to login by checking dictionary.

# users = {
#     "Sanket": "pass123",
#     "Ajay": "pass456",
#     "Akash": "pass789"
# }

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username in users:
#     if users[username] == password:
#         print("Login successful!")
#     else:
#         print("Incorrect password.")
# else:
#     print("Username not found.")
    

#                         --------------------------------------------------------------------

# Store 5 products and prices. Ask the user to enter product names → print total bill.

# products = {
#     "water": 20,
#     "Soda": 25,
#     "milk": 55,
#     "bread": 20,
#     "Onion": 40
# }

# user_input = input("Enter the product names you want to buy (comma-separated): ")
# items = user_input.lower().split(",")

# total = 0
# for item in items:
#     item = item.strip()
#     if item in products:
#         total += products[item]
#     else:
#         print(f"'{item}' is not available.")

# print("Total bill:", total)





#                         --------------------------------------------------------------------

# Store cricket players and their scores. Ask the user to guess who scored the highest.


# scores = {
#     "Kohli": 89,
#     "Smith": 75,
#     "Root": 92,
#     "Babar": 81,
#     "Williamson": 77
# }

# guess = input("Guess which player scored the highest: ")

# top_player = max(scores, key=scores.get)

# if guess.strip().capitalize() == top_player:
#     print("Correct! 🎉", top_player, "scored the highest with", scores[top_player])
# else:
#     print("Wrong guess. 😞 It was", top_player, "with", scores[top_player])


#                         --------------------------------------------------------------------

# Store suspects (name, place, item). Write code to find who is the thief (like detective puzzle).

# suspects = {
#     "Alice": ("Kitchen", "Knife"),
#     "Bob": ("Garden", "Shovel"),
#     "Charlie": ("Library", "Book"),
#     "Diana": ("Kitchen", "Jewels"),
#     "Evan": ("Garage", "Wrench")
# }

# theft_place = "Kitchen"
# stolen_item = "Jewels"

# for name, (place, item) in suspects.items():
#     if place == theft_place and item == stolen_item:
#         print("The thief is:", name)
#         break


#                         --------------------------------------------------------------------

