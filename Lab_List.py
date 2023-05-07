'''
Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.
Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].
Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
'''
my_list =[2,3,4,5,15,1,43,20]

def sum_of_items(list1 :list ) ->int:
    sum = 0
    for element in list1:
        sum +=element
    return sum 

print(f"The sum of items is: {sum_of_items(my_list)}")

def largest_number(list2 : list) -> int:
    max_number = 0
    for element in my_list:
        if element > max_number:
            max_number = element
    return max_number

print(f"The largest number is: {largest_number(my_list)}")

odd_numbers_list= [number for number in range(1200,2000,125) if number%2 != 0]

print(f"The list with odd numbers: {odd_numbers_list}")

new_list = my_list[:5]

print(f"The new list: {new_list}")