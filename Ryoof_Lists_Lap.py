
# LAB_LISTS



### Q1: Write a function that takes a list as a parameter, and then returns  the sum  
# of all the items in that list.
num_list= [2, 3, 4, 5, 15, 1, 43, 20]

def numbers_summation(num_list:int)->int:
    for n in num_list:
        total =sum(num_list)
    return total

print("The Summation of all numbers in the list equal=", numbers_summation(num_list))
print(" ")


### Q2: Write a function that takes a list as a parameter, and then returns the
# largest number from a list of numbers.
num_list2= [2, 3, 4, 5, 15, 1, 43, 20]

def find_large_num(num_list2:int)->int:
    for n in num_list2:
        max_num=max(num_list2)
    return max_num
        
print("The Large number in the list is :" ,find_large_num(num_list2))

### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, 
#using [ list comprehension ].
odd_numbers=[i for i in range(1200,2000,125) if i % 2 != 0 ]
print(odd_numbers)


### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th 
# element in the list.
num_list3= [2, 3, 4, 5, 15, 1, 43, 20]
print (num_list3[0:5:])