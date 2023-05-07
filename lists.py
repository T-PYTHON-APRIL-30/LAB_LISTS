'''
Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.
Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].
Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
'''

#Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.
def sum_list(numbers):
    return sum(numbers)
numbers_list = [2, 3, 4, 5, 15, 1, 43, 20]
result = sum_list(numbers_list)
print(result)


#Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.

def largest_number(numbers):
    return max(numbers)

numbers_list = [2, 3, 4, 5, 15, 1, 43, 20]
result = largest_number(numbers_list)
print(result)


#Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].

odd_numbers = [x for x in range(1200, 2000, 125) if x % 2 != 0]
print(odd_numbers)

#Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
sliced_list = numbers_list[:5]
print(sliced_list)


