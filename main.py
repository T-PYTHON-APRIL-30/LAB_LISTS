list_number = [2, 3, 4, 5, 15, 1, 43, 20]

#Q1
def addition_list(numbers: list) -> int:
    '''function that takes a list as a parameter, and then returns the sum of all the items in that list'''

    solution: int = 0
    for number in numbers:
        solution += number
    return solution


#Q2
def largest_number(numbers: list) -> int:
    '''function that takes a list as a parameter, and then returns the largest number from a list of numbers.'''

    largest: int = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


#Q3
odd_list = [odd_number for odd_number in range(1200, 2000, 125) if odd_number%2 != 0]

#Q4
slicing_list = odd_list[:5]

print(f"The sum of the given list is '{addition_list(list_number)}'")
print(f"The largest number in the given list is '{largest_number(list_number)}'")
print(f"Odd numbers of a range from 1200 to 2000 with steps of 125: {odd_list}")
print(f"Solution Q4: {slicing_list}")