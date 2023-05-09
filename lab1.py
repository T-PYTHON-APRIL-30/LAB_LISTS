num_list = [2, 3, 4, 5, 15, 1, 43, 20]
# Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.
def list_parameters(num_list:list):
    return num_list
print(list_parameters([2,3,4,5,15,1,43,20]))

#Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
def largest_number(num_list:list):
    print("The largest Number is: ", max(num_list))
largest_number(num_list)

#Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].

number= [num for num in range(1200,2000,125) if num%2 !=0 ]
print(number)


#Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
new_num_list = num_list[:5]
print(new_num_list)