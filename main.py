''' Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.
Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].
Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.'''


numbers_list = [2, 3, 4, 5, 15, 1, 43, 20]

#Q1
def addition(numbers :list) -> int:
    '''Function that takes a list as a parameter, and then returns the sum of all the items in that list.'''
    result = 0
    for i in numbers:
        result += i
    return result


#Q2
def largest_number(numbers :list) -> int:
    '''Function that takes a list as a parameter, and then returns the largest number from a list of numbers.'''
    numbers.sort()
    return numbers[-1]

#Q3
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
print("\nThe odd numbers from 1200 to 2000 with steps of 125: ")
odd_list = [number for number in range(1200,2000,125) if number % 2 != 0] 
print(odd_list)

#Q4
new_list = numbers_list [:5]
print(f"\nUsing slicing the list from the start to the 5th element: {new_list}")


print(f"\nThe result of the addition: {addition(numbers_list)}")
print(f"The largest number on the list is: {largest_number(numbers_list)}\n")