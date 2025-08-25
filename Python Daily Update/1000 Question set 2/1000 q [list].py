

# Lists

#                         --------------------------------------------------------------------

# Q1. Get the last element of list a = [1, 2, 2, 3, 1].

# a = [1,2,2,3,1]

# last_element = a[-1]

# print(f"last_element: {last_element}")


#                         --------------------------------------------------------------------

# Q2. Reverse list a = [1, 2, 2, 3, 1] in-place.

# a = [1, 2, 2, 3, 1]

# a.reverse()

# print(f"Reversed List :{a} ")


#                         --------------------------------------------------------------------

# Q3. Return a sorted copy of a = [1, 2, 2, 3, 1].

# a = [1, 2, 2, 3, 1]

# sorted_list = sorted(a)

# print(sorted_list)

#                         --------------------------------------------------------------------

# Q4. Append 1 to list a = [1, 2, 2, 3, 1].

# a = [1, 2, 2, 3, 1]

# a.append('1')

# print(a)

#                         --------------------------------------------------------------------

# Q5. Remove first occurrence of 1 from a = [1, 2, 2, 3, 1].

# a = [1, 2, 2, 3, 1]

# a.remove(1)

# print(a)


#                         --------------------------------------------------------------------

# Q6. Get slice of a = [1, 2, 2, 3, 1] from index 1 to 3.

# a = [1, 2, 2, 3, 1]

# slice_a = a[1:3]  # will start from 1 end with 1 to 3 index value

# print(slice_a)

#                         --------------------------------------------------------------------

# Q7. Compute sum of a = [1, 2, 2, 3, 1].

# a = [1, 2, 2, 3, 1]

# total = sum(a)

# print(f"Total sum of list is: {total}")


#                         --------------------------------------------------------------------

# Q8. Find unique elements of a = [1, 2, 2, 3, 1] preserving order.

# a = [1, 2, 2, 3, 1]

# unique= []

# for num in a:
#     if num not in unique:
#         unique.append(num)

# print(unique)

                                #                         --------------------------------------------------------------------

# a = [1, 2, 2, 3, 1]
# a_set = set(a)

# a_list = list(a_set)
# print(f"a unique list: {a_list}")

#                         --------------------------------------------------------------------

# Q9. Merge two lists a=[1, 2, 2, 3, 1] and b=[2, 3, 4, 6, 2].

# a=[1, 2, 2, 3, 1] 

# b=[2, 3, 4, 6, 2]

# merge = a + b

# print(merge)


#                         --------------------------------------------------------------------

# Q10. Find intersection of lists a=[1, 2, 2, 3, 1] and b=[2, 3, 4, 6, 2].

# from collections import Counter

# a=[1, 2, 2, 3, 1]
# b=[2, 3, 4, 6, 2]

# counter_a = Counter(a)   # # Using Counter to find common elements

# counter_b = Counter(b)

# intersection = []

# for element in counter_a:
#     if element in counter_b:
#         times = min(counter_a[element], counter_b[element])
#         intersection.extend([element] * times)


# print("Intersection (with duplicates):", intersection)


#                         --------------------------------------------------------------------

# Q11. Count occurrences of 1 in a = [1, 2, 2, 3, 1].

# a = [1, 2, 2, 3, 1]

# count_a = a.count(1)

# print(count_a)


# length = len(a)
# print(length)


#                         --------------------------------------------------------------------

# Q12. Replace index 2 in a=[1, 2, 2, 3, 1] with 99.

# a=[1, 2, 2, 3, 1]

# a[2] = 99

# print(a)


#                         --------------------------------------------------------------------

# Q13. Get even numbers from nums = [1, 2, 3, 4, 5, 6].

# nums = [1, 2, 3, 4, 5, 6]

# even_num = [n for n in nums if n % 2 == 0]

# print(even_num)


#                         --------------------------------------------------------------------

# Q14. Square each number in nums = [1, 2, 3, 4, 5, 6].


# nums = [1, 2, 3, 4, 5, 6]

# square = [n ** 2 for n in nums]

# print(square)


#                         --------------------------------------------------------------------

# Q15. Flatten nested list [[1,2],[3,4],[5]] in one line.

# nested = [[1, 2], [3, 4], [5]]

# flat = [item for sublist in nested for item in sublist]

# print("Flattened list:", flat)


#                         --------------------------------------------------------------------

# Q16. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5, 6].

# nums = [1, 2, 3, 4, 5, 6]

# pairs = [(x, x**2) for x in nums]

# print("List of (x, x^2) pairs:", pairs)



#                         --------------------------------------------------------------------

# Q17. Rotate list a=[1, 2, 2, 3, 1] right by 2.

# a=[1, 2, 2, 3, 1]

# k = 2

# rotated = a[-k:] + a[:-k]

# print("Rotated list (right by 2):", rotated)


#                         --------------------------------------------------------------------

# Q18. Get second largest from nums = [1, 2, 3, 4, 5, 6].

# nums = [1, 2, 3, 4, 5, 6]

# unique_nums = list(set(nums))  # remove duplicates 
# unique_nums.sort(reverse=True)  # Reverse a list

# second_largest = unique_nums[1] if len(unique_nums) > 1 else None # by indexing get 2nd value
# print("Second largest number:", second_largest)



#                         --------------------------------------------------------------------

# Q19. Remove None values from [1,None,2,None,3].

# a = [1, None, 2, None, 3]

# New_list = [x for x in a if x is not None]

# print("List after removing None:", New_list)


#                         --------------------------------------------------------------------

# Q20. Zip [1, 2, 3, 4, 5, 6] and ['beta', 'gamma', 'delta', 'epsilon', 'zeta'] into list of tuples.

# numbers = [1, 2, 3, 4, 5, 6]
# labels = ['beta', 'gamma', 'delta', 'epsilon', 'zeta']

# zipped = list(zip(numbers,labels))


# print("Zipped list of tuples:", zipped)


#                         --------------------------------------------------------------------

# Q21. Get the last element of list a = [2, 3, 4, 6, 2].

# a = [2, 3, 4, 6, 2]

# print(a[-1])    #  by using negative indexing -1


#                         --------------------------------------------------------------------

# Q22. Reverse list a = [2, 3, 4, 6, 2] in-place.

# a = [2, 3, 4, 6, 2]

# a.reverse()

# print(a)

#                         --------------------------------------------------------------------

# Q23. Return a sorted copy of a = [2, 3, 4, 6, 2].

# a = [2, 3, 4, 6, 2]

# sorted_list = sorted(a)

# print(sorted_list)


#                         --------------------------------------------------------------------

# Q24. Append 2 to list a = [2, 3, 4, 6, 2].

# a = [2, 3, 4, 6, 2]

# a.append(2)

# print(a)


#                         --------------------------------------------------------------------

# Q25. Remove first occurrence of 2 from a = [2, 3, 4, 6, 2].

# a = [2, 3, 4, 6, 2]

# a.remove(2)

# print(a)


#                         --------------------------------------------------------------------

# Q26. Get slice of a = [2, 3, 4, 6, 2] from index 1 to 3.

# a = [2, 3, 4, 6, 2]

# slice_a = a[1:3]

# print(slice_a)

#                         --------------------------------------------------------------------

# Q27. Compute sum of a = [2, 3, 4, 6, 2].

# a = [2, 3, 4, 6, 2]

# Total = sum(a)

# print(Total)

#                         --------------------------------------------------------------------


# Q28. Find unique elements of a = [2, 3, 4, 6, 2] preserving order.

# a = [2, 3, 4, 6, 2]

# unique = []

# for item in a:
#     if item not in unique:
#         unique.append(item)
# print("Unique elements preserving order:", unique)


#                         --------------------------------------------------------------------

# Q29. Merge two lists a=[2, 3, 4, 6, 2] and b=[3, 4, 6, 9, 3].

# a=[2, 3, 4, 6, 2] 
# b=[3, 4, 6, 9, 3]

# merge = a + b

# print(merge)

#                         --------------------------------------------------------------------

# Q30. Find intersection of lists a=[2, 3, 4, 6, 2] and b=[3, 4, 6, 9, 3].

# a = [2, 3, 4, 6, 2]
# b = [3, 4, 6, 9, 3]

# intersection = list(set(a) & set(b))

# print("Intersection:", intersection)


#                         --------------------------------------------------------------------

# Q31. Count occurrences of 2 in a = [2, 3, 4, 6, 2].

# a = [2, 3, 4, 6, 2]

# count_2 = a.count(2)

# print(count_2)

#                         --------------------------------------------------------------------

# Q32. Replace index 2 in a=[2, 3, 4, 6, 2] with 99.

# a=[2, 3, 4, 6, 2]

# a[2] = 99

# print(a)


#                         --------------------------------------------------------------------

# Q33. Get even numbers from nums = [1, 2, 3, 4, 5, 6, 7].

# nums = [1, 2, 3, 4, 5, 6, 7]

# even_num = [x for x in nums if x % 2 == 0]

# print(even_num)


#                         --------------------------------------------------------------------

# Q34. Square each number in nums = [1, 2, 3, 4, 5, 6, 7].

# nums = [1, 2, 3, 4, 5, 6, 7]

# squares = [x**2 for x in nums]

# print("Squared numbers:", squares)

#                         --------------------------------------------------------------------

# Q35. Flatten nested list [[1,2],[3,4],[5]] in one line.

# nested = [[1, 2], [3, 4], [5]]
# flattened = [item for sublist in nested for item in sublist]
# print("Flattened list:", flattened)



#                         --------------------------------------------------------------------

# Q36. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5, 6, 7].


# nums = [1, 2, 3, 4, 5, 6, 7]

# pairs = [(x, x**2) for x in nums]

# print("Pairs (x, x^2):", pairs)


#                         --------------------------------------------------------------------

# Q37. Rotate list a=[2, 3, 4, 6, 2] right by 2.


# a = [2, 3, 4, 6, 2]

# rotated = a[-2:] + a[:-2]

# print("Rotated right by 2:", rotated)


#                         --------------------------------------------------------------------

# Q38. Get second largest from nums = [1, 2, 3, 4, 5, 6, 7].

# nums = [1, 2, 3, 4, 5, 6, 7]

# second_largest = sorted(set(nums))[-2]  # by using -2 indexing getting second max through sorted set

# print("Second largest number:", second_largest)

#                         --------------------------------------------------------------------

# Q39. Remove None values from [1,None,2,None,3].

# data = [1, None, 2, None, 3]

# cleaned = [x for x in data if x is not None]

# print("List without None:", cleaned)


#                         --------------------------------------------------------------------

# Q40. Zip [1, 2, 3, 4, 5, 6, 7] and ['gamma', 'delta', 'epsilon', 'zeta', 'eta'] into list of tuples.

# nums = [1, 2, 3, 4, 5, 6, 7]
# names = ['gamma', 'delta', 'epsilon', 'zeta', 'eta']

# zipped_value = list(zip(nums,names))

# print(zipped_value)


#                         --------------------------------------------------------------------

# Q41. Get the last element of list a = [3, 4, 6, 9, 3].

# a = [3, 4, 6, 9, 3]
# last = a[-1]
# print("Last element:", last)

#                         --------------------------------------------------------------------

# Q42. Reverse list a = [3, 4, 6, 9, 3] in-place.

# a = [3, 4, 6, 9, 3]

# a.reverse()

# print(a)

#                         --------------------------------------------------------------------

# Q43. Return a sorted copy of a = [3, 4, 6, 9, 3].

# a = [3, 4, 6, 9, 3]

# sorted_copy = sorted(a)

# print(sorted_copy)

#                         --------------------------------------------------------------------

# Q44. Append 3 to list a = [3, 4, 6, 9, 3].

# a = [3, 4, 6, 9, 3]

# a.append(3)

# print(a)

#                         --------------------------------------------------------------------

# Q45. Remove first occurrence of 3 from a = [3, 4, 6, 9, 3].

# a = [3, 4, 6, 9, 3]

# a.remove(3)

# print(a)

#                         --------------------------------------------------------------------

# Q46. Get slice of a = [3, 4, 6, 9, 3] from index 1 to 3.


# a = [3, 4, 6, 9, 3]
# slice_a = a[1:3]
# print("Slice from index 1 to 3:", slice_a)


#                         --------------------------------------------------------------------

# Q47. Compute sum of a = [3, 4, 6, 9, 3].

# a = [3, 4, 6, 9, 3]
# total = sum(a)
# print("Sum:", total)


#                         --------------------------------------------------------------------

# Q48. Find unique elements of a = [3, 4, 6, 9, 3] preserving order.

# a = [3, 4, 6, 9, 3]
# unique = []
# for i in a:
#     if i not in unique:
#         unique.append(i)
# print("Unique elements:", unique)


#                         --------------------------------------------------------------------

# Q49. Merge two lists a=[3, 4, 6, 9, 3] and b=[4, 5, 8, 12, 4].


# a = [3, 4, 6, 9, 3]
# b = [4, 5, 8, 12, 4]

# merge = a + b

# print("Merged list:", merge)


#                         --------------------------------------------------------------------

# Q50. Find intersection of lists a=[3, 4, 6, 9, 3] and b=[4, 5, 8, 12, 4].

# a = [3, 4, 6, 9, 3]
# b = [4, 5, 8, 12, 4]

# intersection = list(set(a) & set(b))

# print("Intersection:", intersection)


#                         --------------------------------------------------------------------

# Q51. Count occurrences of 3 in a = [3, 4, 6, 9, 3].

# a = [3, 4, 6, 9, 3]

# count_3 = a.count(3)

# print("Occurrences of 3:", count_3)


#                         --------------------------------------------------------------------

# Q52. Replace index 2 in a=[3, 4, 6, 9, 3] with 99.

# a=[3, 4, 6, 9, 3]

# a[2] = 99

# print(a)

#                         --------------------------------------------------------------------

# Q53. Get even numbers from nums = [1, 2, 3, 4, 5, 6, 7, 8].

# nums = [1, 2, 3, 4, 5, 6, 7, 8]

# even_nums = [x for x in nums if x % 2 == 0]

# print("Even numbers:", even_nums)

#                         --------------------------------------------------------------------

# Q54. Square each number in nums = [1, 2, 3, 4, 5, 6, 7, 8].

# nums = [1, 2, 3, 4, 5, 6, 7, 8]

# squared = [x**2 for x in nums]

# print("Squared numbers:", squared)


#                         --------------------------------------------------------------------

# Q55. Flatten nested list [[1,2],[3,4],[5]] in one line.

# nested = [[1, 2], [3, 4], [5]]

# flat = [x for sublist in nested for x in sublist]

# print("Flattened list:", flat)

#                         --------------------------------------------------------------------

# Q56. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5, 6, 7, 8].

# nums = [1, 2, 3, 4, 5, 6, 7, 8]

# pairs = [(x, x**2) for x in nums]

# print("List of (x, x^2) pairs:", pairs)


#                         --------------------------------------------------------------------

# Q57. Rotate list a=[3, 4, 6, 9, 3] right by 2.

# a = [3, 4, 6, 9, 3]

# k = 2
# rotated = a[-k:] + a[:-k]

# print("Rotated list:", rotated)


#                         --------------------------------------------------------------------

# Q58. Get second largest from nums = [1, 2, 3, 4, 5, 6, 7, 8].

# nums = [1, 2, 3, 4, 5, 6, 7, 8]

# second_largest = sorted(set(nums))[-2]

# print("Second largest number:", second_largest)


#                         --------------------------------------------------------------------

# Q59. Remove None values from [1,None,2,None,3].

# data = [1, None, 2, None, 3]

# cleaned = [x for x in data if x is not None]

# print("List after removing None:", cleaned)


#                         --------------------------------------------------------------------

# Q60. Zip [1, 2, 3, 4, 5, 6, 7, 8] and ['delta', 'epsilon', 'zeta', 'eta', 'theta'] into list of tuples.


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# labels = ['delta', 'epsilon', 'zeta', 'eta', 'theta']

# zipped = list(zip(numbers, labels))

# print("Zipped list:", zipped)


#                         --------------------------------------------------------------------

# Q61. Get the last element of list a = [4, 5, 8, 12, 4].

# a = [4, 5, 8, 12, 4]
# last = a[-1]
# print("Last element:", last)


#                         --------------------------------------------------------------------

# Q62. Reverse list a = [4, 5, 8, 12, 4] in-place.

# a = [4, 5, 8, 12, 4]

# a.reverse()

# print("Reversed list:", a)


#                         --------------------------------------------------------------------

# Q63. Return a sorted copy of a = [4, 5, 8, 12, 4].

# a = [4, 5, 8, 12, 4]

# sorted_copy = sorted(a)

# print("Sorted copy:", sorted_copy)


#                         --------------------------------------------------------------------

# Q64. Append 4 to list a = [4, 5, 8, 12, 4].

# a = [4, 5, 8, 12, 4]

# a.append(4)

# print("After appending 4:", a)

#                         --------------------------------------------------------------------

# Q65. Remove first occurrence of 4 from a = [4, 5, 8, 12, 4].

# a = [4, 5, 8, 12, 4]

# a.remove(4)

# print("After removing first 4:", a)

#                         --------------------------------------------------------------------

# Q66. Get slice of a = [4, 5, 8, 12, 4] from index 1 to 3.

# a = [4, 5, 8, 12, 4]
# slice_a = a[1:3]
# print("Slice from index 1 to 3:", slice_a)

#                         --------------------------------------------------------------------

# Q67. Compute sum of a = [4, 5, 8, 12, 4].

# a = [4, 5, 8, 12, 4]
# total = sum(a)
# print("Sum of a:", total)


#                         --------------------------------------------------------------------

# Q68. Find unique elements of a = [4, 5, 8, 12, 4] preserving order.

# a = [4, 5, 8, 12, 4]
# unique = []
# for x in a:
#     if x not in unique:
#         unique.append(x)
# print("Unique elements:", unique)


#                         --------------------------------------------------------------------

# Q69. Merge two lists a=[4, 5, 8, 12, 4] and b=[5, 6, 10, 2, 0].

# a = [4, 5, 8, 12, 4]
# b = [5, 6, 10, 2, 0]

# merged = a + b

# print("Merged list:", merged)


#                         --------------------------------------------------------------------

# Q70. Find intersection of lists a=[4, 5, 8, 12, 4] and b=[5, 6, 10, 2, 0].

# a = [4, 5, 8, 12, 4]
# b = [5, 6, 10, 2, 0]

# intersection = list(set(a) & set(b))

# print("Intersection:", intersection)


#                         --------------------------------------------------------------------

# Q71. Count occurrences of 4 in a = [4, 5, 8, 12, 4].

# a = [4, 5, 8, 12, 4]

# count_a =  a.count(4)

# print(count_a)

#                         --------------------------------------------------------------------

# Q72. Replace index 2 in a=[4, 5, 8, 12, 4] with 99.


# a = [4, 5, 8, 12, 4]

# a[2] = 99

# print(a)


#                         --------------------------------------------------------------------

# Q73. Get even numbers from nums = [1, 2, 3, 4, 5, 6, 7, 8, 9].

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# even_nums = [x for x in nums if x % 2 == 0]

# print(even_nums)


#                         --------------------------------------------------------------------

# Q74. Square each number in nums = [1, 2, 3, 4, 5, 6, 7, 8, 9].

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# square = [ x ** 2 for x in nums]

# print(square)


#                         --------------------------------------------------------------------

# # Q75. Flatten nested list [[1,2],[3,4],[5]] in one line.


#                         --------------------------------------------------------------------


# Q76. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5, 6, 7, 8, 9].

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# pairs = [(x, x**2) for x in nums]

# print("List of (x, x^2) pairs:", pairs)


#                         --------------------------------------------------------------------

# Q77. Rotate list a=[4, 5, 8, 12, 4] right by 2.

# a = [4, 5, 8, 12, 4]

# k = 2

# rotated = a[-k:] + a[:-k]

# print(rotated)

#                         --------------------------------------------------------------------

# Q78. Get second largest from nums = [1, 2, 3, 4, 5, 6, 7, 8, 9].

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# second_largest = sorted(set(nums))[-2]

# print(second_largest)

#                         --------------------------------------------------------------------

# Q79. Remove None values from [1,None,2,None,3].

# data = [1, None, 2, None, 3]

# cleaned = [x for x in data if x is not None]

# print("List after removing None:", cleaned)


#                         --------------------------------------------------------------------

# Q80. Zip [1, 2, 3, 4, 5, 6, 7, 8, 9] and ['epsilon', 'zeta', 'eta', 'theta', 'alpha'] into list of tuples.


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# labels = ['epsilon', 'zeta', 'eta', 'theta', 'alpha']

# zipped = list(zip(numbers, labels))

# print("Zipped list:", zipped)


#                         --------------------------------------------------------------------

# Q81. Get the last element of list a = [5, 6, 10, 2, 0].

# a = [5, 6, 10, 2, 0]

# print(a[-1])



#                         --------------------------------------------------------------------

# Q82. Reverse list a = [5, 6, 10, 2, 0] in-place.

# a = [5, 6, 10, 2, 0]

# a.reverse()

# print(a)


#                         --------------------------------------------------------------------

# Q83. Return a sorted copy of a = [5, 6, 10, 2, 0].

# a = [5, 6, 10, 2, 0]

# sorted_copy = sorted(a)

# print("Sorted copy:", sorted_copy)


#                         --------------------------------------------------------------------

# Q84. Append 5 to list a = [5, 6, 10, 2, 0].

# a = [5, 6, 10, 2, 0]

# a.append(5)

# print("After appending 5:", a)


#                         --------------------------------------------------------------------

# Q85. Remove first occurrence of 0 from a = [5, 6, 10, 2, 0].

# a = [5, 6, 10, 2, 0]

# a.remove(0)

# print(a)

#                         --------------------------------------------------------------------

# Q86. Get slice of a = [5, 6, 10, 2, 0] from index 1 to 3.


# a = [5, 6, 10, 2, 0]

# slice_ = a[1:4]  # includes index 1, 2, 3

# print("Slice from index 1 to 3:", slice_)


#                         --------------------------------------------------------------------

# Q87. Compute sum of a = [5, 6, 10, 2, 0].

# a = [5, 6, 10, 2, 0]

# total = sum(a)

# print(total)

#                         --------------------------------------------------------------------

# Q88. Find unique elements of a = [5, 6, 10, 2, 0] preserving order.

# a = [5, 6, 10, 2, 0]

# unique = []

# for x in a:
#     if x not in unique:
#         unique.append(x)
# print("Unique elements:", unique)


#                         --------------------------------------------------------------------

# Q89. Merge two lists a=[5, 6, 10, 2, 0] and b=[6, 7, 1, 5, 1].

# a = [5, 6, 10, 2, 0]
# b = [6, 7, 1, 5, 1]

# merge = a + b

# print("Merged list:", merge)


#                         --------------------------------------------------------------------

# Q90. Find intersection of lists a=[5, 6, 10, 2, 0] and b=[6, 7, 1, 5, 1].

# from collections import Counter

# a = [5, 6, 10, 2, 0]
# b = [6, 7, 1, 5, 1]

# counter_a = Counter(a)
# counter_b = Counter(b)

# intersection = []

# for x in counter_a:
#     if x in counter_b:
#         intersection.extend([x] * min(counter_a[x], counter_b[x]))

# print("Intersection (with duplicates):", intersection)


#                         --------------------------------------------------------------------

# Q91. Count occurrences of 5 in a = [5, 6, 10, 2, 0].

# a = [5, 6, 10, 2, 0]

# count_5 = a.count(5)

# print(count_5)

#                         --------------------------------------------------------------------

# Q92. Replace index 2 in a=[5, 6, 10, 2, 0] with 99.

# a = [5, 6, 10, 2, 0]

# a[2] = 99

# print("After replacement:", a)


#                         --------------------------------------------------------------------

# Q93. Get even numbers from nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even = [x for x in nums if x % 2 == 0]

# print(even)

#                         --------------------------------------------------------------------

# Q94. Square each number in nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# squares = [x**2 for x in nums]

# print("Squares:", squares)


#                         --------------------------------------------------------------------

# Q95. Flatten nested list [[1,2],[3,4],[5]] in one line.

# nested = [[1, 2], [3, 4], [5]]
# flattened = [item for sublist in nested for item in sublist]
# print("Flattened list:", flattened)


#                         --------------------------------------------------------------------


# Q96. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

# nums = [1,2,3,4,5,6,7,8,9,10]

# pairs = [(x, x**2) for x in nums]

# print(pairs)

#                         --------------------------------------------------------------------

# Q97. Rotate list a=[5, 6, 10, 2, 0] right by 2.

# a = [5, 6, 10, 2, 0]

# k = 2

# rotated = a[-k:] + a[:-k]

# print(rotated)

#                         --------------------------------------------------------------------

# Q98. Get second largest from nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

# nums = [1,2,3,4,5,6,7,8,9,10]
# second_largest = sorted(set(nums))[-2]
# print(second_largest)

#                         --------------------------------------------------------------------

# Q99. Remove None values from [1,None,2,None,3].

# lst = [1, None, 2, None, 3]

# New = [x for x in lst if x is not None]

# print(New)

#                         --------------------------------------------------------------------

# Q100. Zip [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and ['zeta', 'eta', 'theta', 'alpha', 'beta'] into list of tuples.

# nums = [1,2,3,4,5,6,7,8,9,10]

# words = ['zeta', 'eta', 'theta', 'alpha', 'beta']

# zipped = list(zip(nums, words))

# print(zipped)


#                         --------------------------------------------------------------------


# Q101. Get the last element of list a = [6, 7, 1, 5, 1].

# a = [6, 7, 1, 5, 1]

# last_element = a[-1]

# print(f"Last element: {last_element}")



#                         --------------------------------------------------------------------

# Q102. Reverse list a = [6, 7, 1, 5, 1] in-place.

# a = [6, 7, 1, 5, 1]

# a.reverse()

# print(f"Reversed ordered list: {a}")


#                         --------------------------------------------------------------------

# Q103. Return a sorted copy of a = [6, 7, 1, 5, 1].

# a = [6, 7, 1, 5, 1]

# sorted_list = sorted(a)

# print(sorted_list)


#                         --------------------------------------------------------------------

# Q104. Append 6 to list a = [6, 7, 1, 5, 1].

# a = [6, 7, 1, 5, 1]

# a.append(6)

# print(a)


#                         --------------------------------------------------------------------

# Q105. Remove first occurrence of 1 from a = [6, 7, 1, 5, 1].

# a = [6, 7, 1, 5, 1]

# a.remove(1)

# print(a)


#                         --------------------------------------------------------------------

# Q106. Get slice of a = [6, 7, 1, 5, 1] from index 1 to 3.

# a = [6, 7, 1, 5, 1]

# slicing_list = a[1:4]

# print(slicing_list)

#                         --------------------------------------------------------------------

# Q107. Compute sum of a = [6, 7, 1, 5, 1].

# a = [6, 7, 1, 5, 1]

# Total = sum(a)

# print(f"Sum of list: {Total}")



#                         --------------------------------------------------------------------

# Q108. Find unique elements of a = [6, 7, 1, 5, 1] preserving order.

# a = [6, 7, 1, 5, 1]

# unique = []

# for item in a:
#     if item not in unique:
#         unique.append(item)

# print(unique)

#                         --------------------------------------------------------------------

# Q109. Merge two lists a=[6, 7, 1, 5, 1] and b=[0, 8, 3, 8, 2].

# a=[6, 7, 1, 5, 1] 
# b=[0, 8, 3, 8, 2]

# merged_list = a + b

# print(merged_list)



#                         --------------------------------------------------------------------

# Q110. Find intersection of lists a=[6, 7, 1, 5, 1] and b=[0, 8, 3, 8, 2].

# a=[6, 7, 1, 5, 1]
# b=[0, 8, 3, 8, 2]

# intersection = list(set(a) & set(b))

# print(f"Intersection between both list is: ",intersection)

#                         --------------------------------------------------------------------

# Q111. Count occurrences of 6 in a = [6, 7, 1, 5, 1]

# a = [6, 7, 1, 5, 1]

# count_6 = a.count(6)

# print(f"Count 0f 6 :{count_6}")


#                         --------------------------------------------------------------------

# Q112. Replace index 2 in a=[6, 7, 1, 5, 1] with 99.

# a = [6, 7, 1, 5, 1]

# a[2] = 99    # # index value 2 

# print(a)

#                         --------------------------------------------------------------------

# Q113. Get even numbers from nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# even_nums = [x for x in nums if x % 2 == 0]

# print(even_nums)

#                         --------------------------------------------------------------------

# Q114. Square each number in nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# square = [ x ** 2 for x in nums ]

# print(square)

#                         --------------------------------------------------------------------

# Q115. Flatten nested list [[1,2],[3,4],[5]] in one line.


# nested = [[1, 2], [3, 4], [5]]

# flat = [x for sublist in nested for x in sublist]

# print("Flattened list:", flat)



#                         --------------------------------------------------------------------

# Q116. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# pairs = [(x, x**2) for x in nums]

# print(f"Pairs : {pairs}")



#                         --------------------------------------------------------------------

# Q117. Rotate list a=[6, 7, 1, 5, 1] right by 2.

# a=[6, 7, 1, 5, 1]

# k = 2

# rotate = a[-k:] + a[:-k]

# print(rotate)

#                         --------------------------------------------------------------------

# Q118. Get second largest from nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# second_max = sorted(set(nums))[-2]

# print(second_max)


#                         --------------------------------------------------------------------

# Q119. Remove None values from [1,None,2,None,3].

# list = [1,None,2,None,3]

# cleaned = [x for x in list if x is not None]

# print(cleaned)


#                         --------------------------------------------------------------------

# Q120. Zip [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and ['eta', 'theta', 'alpha', 'beta', 'gamma'] into list of tuples.

# nums =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# words = ['eta', 'theta', 'alpha', 'beta', 'gamma']

# zipped = list(zip(nums,words))

# print(zipped)



#                         --------------------------------------------------------------------


# Q121. Get the last element of list a = [0, 8, 3, 8, 2].

# a = [0, 8, 3, 8, 2]

# last_element = a[-1]

# print(last_element)



#                         --------------------------------------------------------------------

# Q122. Reverse list a = [0, 8, 3, 8, 2] in-place.

# a = [0, 8, 3, 8, 2]

# a.reverse()

# print(a)

#                         --------------------------------------------------------------------

# Q123. Return a sorted copy of a = [0, 8, 3, 8, 2].

# a = [0, 8, 3, 8, 2]

# sorted_list = sorted(a)

# print(sorted_list)

#                         --------------------------------------------------------------------

# Q124. Append 7 to list a = [0, 8, 3, 8, 2].

# a = [0, 8, 3, 8, 2]

# a.append(7)

# print(a)

#                         --------------------------------------------------------------------

# Q125. Remove first occurrence of 2 from a = [0, 8, 3, 8, 2].

# a = [0, 8, 3, 8, 2]

# a.remove(2)

# print(a)


#                         --------------------------------------------------------------------

# Q126. Get slice of a = [0, 8, 3, 8, 2] from index 1 to 3.

# a = [0, 8, 3, 8, 2]

# slicing_a = a[1:4]

# print(slicing_a)

#                         --------------------------------------------------------------------

# Q127. Compute sum of a = [0, 8, 3, 8, 2].

# a = [0, 8, 3, 8, 2]

# Total = sum(a)

# print(Total)

#                         --------------------------------------------------------------------

# Q128. Find unique elements of a = [0, 8, 3, 8, 2] preserving order.


# a = [0, 8, 3, 8, 2]

# unique = []
# for item in a:
#     if item not in unique:
#         unique.append(item)

# print(unique)


#                         --------------------------------------------------------------------

# Q129. Merge two lists a=[0, 8, 3, 8, 2] and b=[1, 0, 5, 11, 3].


# a=[0, 8, 3, 8, 2] 
# b=[1, 0, 5, 11, 3]

# merge = a + b

# print(merge)



#                         --------------------------------------------------------------------

# Q130. Find intersection of lists a=[0, 8, 3, 8, 2] and b=[1, 0, 5, 11, 3].

# a=[0, 8, 3, 8, 2] 
# b=[1, 0, 5, 11, 3]

# intersection = list(set(a) & set(b))  # Output (unordered): [0, 3]

# print(intersection)


#                         --------------------------------------------------------------------

# Q131. Count occurrences of 0 in a = [0, 8, 3, 8, 2].

# a = [0, 8, 3, 8, 2]

# count_0 = a.count(0)

# print(count_0)


#                         --------------------------------------------------------------------

# Q132. Replace index 2 in a=[0, 8, 3, 8, 2] with 99.

# a = [0, 8, 3, 8, 2]

# a[2] = 99

# print(a)

#                         --------------------------------------------------------------------

# Q133. Get even numbers from nums = [1, 2, 3, 4, 5].

# nums = [1, 2, 3, 4, 5]

# even_nums = [x for x in nums if x % 2 == 0]

# print(even_nums)

#                         --------------------------------------------------------------------

# Q134. Square each number in nums = [1, 2, 3, 4, 5].

# nums = [1, 2, 3, 4, 5]

# square = [x ** 2 for x in nums]

# print(square)

#                         --------------------------------------------------------------------

# Q135. Flatten nested list [[1,2],[3,4],[5]] in one line.

# nested = [[1,2],[3,4],[5]]

# flattened = [item for sublist in nested for item in sublist]

# print(flattened)


#                         --------------------------------------------------------------------

# Q136. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5].

# nums = [1, 2, 3, 4, 5]

# pairs = [(x, x**2) for x in nums]

# print(pairs)


#                         --------------------------------------------------------------------

# Q137. Rotate list a=[0, 8, 3, 8, 2] right by 2.

# a=[0, 8, 3, 8, 2]

# k = 2

# rotate = a[-k:] + a[:-k]  

# print(rotate)


#                         --------------------------------------------------------------------

# Q138. Get second largest from nums = [1, 2, 3, 4, 5].

# nums = [1, 2, 3, 4, 5]

# second_max = sorted(set(nums))[-2]

# print(second_max)

#                         --------------------------------------------------------------------

# Q139. Remove None values from [1,None,2,None,3].

# list = [1,None,2,None,3]

# cleaned = [x for x in list if x is not None]

# print(cleaned)

#                         --------------------------------------------------------------------

# Q140. Zip [1, 2, 3, 4, 5] and ['theta', 'alpha', 'beta', 'gamma', 'delta'] into list of tuples.

# nums = [1, 2, 3, 4, 5]

# words = ['theta', 'alpha', 'beta', 'gamma', 'delta']

# zipped = list(zip(nums,words))

# print(zipped)

#                         --------------------------------------------------------------------

# Q141. Get the last element of list a = [1, 0, 5, 11, 3].

# a = [1, 0, 5, 11, 3]

# print(a[-1])


#                         --------------------------------------------------------------------

# Q142. Reverse list a = [1, 0, 5, 11, 3] in-place.

# a = [1, 0, 5, 11, 3]

# a.reverse()

# print(a)

#                         --------------------------------------------------------------------

# Q143. Return a sorted copy of a = [1, 0, 5, 11, 3].

# a = [1, 0, 5, 11, 3]

# sorted_list = sorted(a)

# print(sorted_list)

#                         --------------------------------------------------------------------

# Q144. Append 8 to list a = [1, 0, 5, 11, 3].

# a = [1, 0, 5, 11, 3]

# a.append(8)

# print(a)

#                         --------------------------------------------------------------------

# Q145. Remove first occurrence of 3 from a = [1, 0, 5, 11, 3].

# a = [1, 0, 5, 11, 3]

# a.remove(3)

# print(a)

#                         --------------------------------------------------------------------

# Q146. Get slice of a = [1, 0, 5, 11, 3] from index 1 to 3.

# a = [1, 0, 5, 11, 3]

# slicing_a = a[1:4]

# print(slicing_a)


#                         --------------------------------------------------------------------

# Q147. Compute sum of a = [1, 0, 5, 11, 3].

# a = [1, 0, 5, 11, 3]

# Total = sum(a)

# print(Total)

#                         --------------------------------------------------------------------

# Q148. Find unique elements of a = [1, 0, 5, 11, 3] preserving order.

# a = [1, 0, 5, 11, 3]

# unique = []

# for x in a:
#     if x not in unique:
#         unique.append(x)


# print("Unique elements:", unique)

#                         --------------------------------------------------------------------

# Q149. Merge two lists a=[1, 0, 5, 11, 3] and b=[2, 1, 7, 1, 4].

# a=[1, 0, 5, 11, 3] 

# b=[2, 1, 7, 1, 4]

# merge = a + b

# print(merge)


#                         --------------------------------------------------------------------

# Q150. Find intersection of lists a=[1, 0, 5, 11, 3] and b=[2, 1, 7, 1, 4].

# a=[1, 0, 5, 11, 3] 
# b=[2, 1, 7, 1, 4]

# intersection = list(set(a) & set(b))

# print(intersection)



#                         --------------------------------------------------------------------

# Q151. Count occurrences of 1 in a = [1, 0, 5, 11, 3].

# a = [1, 0, 5, 11, 3]

# count_1 = a.count(1)

# print(count_1)


#                         --------------------------------------------------------------------

# Q152. Replace index 2 in a=[1, 0, 5, 11, 3] with 99.

# a = [1, 0, 5, 11, 3]

# a[2] = 99

# print(a)

#                         --------------------------------------------------------------------

# Q153. Get even numbers from nums = [1, 2, 3, 4, 5, 6].

# nums = [1, 2, 3, 4, 5, 6]

# even_nums = [x for x in nums if x % 2 == 0]

# print(even_nums)


#                         --------------------------------------------------------------------

# Q154. Square each number in nums = [1, 2, 3, 4, 5, 6].

# nums = [1, 2, 3, 4, 5, 6]

# square = [ x**2 for x in nums ]

# print(square)


#                         --------------------------------------------------------------------

# Q155. Flatten nested list [[1,2],[3,4],[5]] in one line.

# nested = [[1,2],[3,4],[5]]

# flattened = [item for sublist in nested for item in sublist]

# print(flattened)


#                         --------------------------------------------------------------------

# Q156. Create list of pairs (x, x^2) for nums = [1, 2, 3, 4, 5, 6].

# nums = [1, 2, 3, 4, 5, 6]

# pairs = [(x, x**2) for x in nums]

# print(pairs)



#                         --------------------------------------------------------------------

# Q157. Rotate list a=[1, 0, 5, 11, 3] right by 2.

# a=[1, 0, 5, 11, 3]

# k = 2

# rotate = a[-k:] + a[:-k]

# print(rotate)


#                         --------------------------------------------------------------------

# Q158. Get second largest from nums = [1, 2, 3, 4, 5, 6].

# nums = [1, 2, 3, 4, 5, 6]

# second_max = sorted(set(nums))[-2]

# print(second_max)


#                         --------------------------------------------------------------------

# Q159. Remove None values from [1,None,2,None,3].

# list = [1,None,2,None,3]

# clear = [x for x in list if x is not None]

# print(clear)

#                         --------------------------------------------------------------------

# Q160. Zip [1, 2, 3, 4, 5, 6] and ['alpha', 'beta', 'gamma', 'delta', 'epsilon'] into list of tuples.

# nums = [1, 2, 3, 4, 5, 6]  
# words = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']

# zipped = list(zip(nums,words))

# print(zipped)


#                         --------------------------------------------------------------------
