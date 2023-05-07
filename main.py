
my_list = [2, 3, 4, 5, 15, 1, 43, 20]

### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.
def sum_of_list(list):
    sum = 0
    for element in list:
        sum += element
    return sum

print(f"the sum of the list is: {sum_of_list(my_list)}")


### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
def Max(list):
    max = 0
    for element in list:
        if element > max:
            max = element
    return max

print(f"maximum number in the list: {max(my_list)}")

### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].

# create the original list:
original_list = list(range(1200,2000,125))
print(f"the list of numbers from 1200 to 2000 with 125 steps: {original_list}")
#new list with odd number
odd_numbers_list = [number for number in original_list if number % 2 != 0]
print (f"the list of odd numbers: {odd_numbers_list}")

### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
sliced_list = my_list[0:5]
print(f"sliced list: {sliced_list}")
