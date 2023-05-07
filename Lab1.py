# LAB_LISTS
my_list=[2, 3, 4, 5, 15, 1, 43, 20]

### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.
def addition(list):
    result=0
    for element in my_list:
        result+= element
    print(result)

addition(my_list)

### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
def largest(list):
    largest=0
    for element in my_list:
     if largest<element:
           largest= element
    print(largest)
largest(my_list)

### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].
second_list=[*range(1200,2001)] #the * sympol unpacks the range function inside the list
oddlist = [number for number in second_list[::125] if number%2 !=0]
print(oddlist)

### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
fifth_element_list=oddlist[:4]
print(fifth_element_list)
