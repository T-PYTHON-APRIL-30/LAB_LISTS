'''Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
* Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.
* Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
*Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].
*Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.'''

def sumList (myList:list) -> int:
    sum = 0
    for num in myList:
        sum += num

    return sum

def largestNum (myList:list) -> int:
    return max(myList)

def oddNumbers () -> list:
    newList = []

    for n in range (1200,2000,125): 
        if n%2 != 0:
            newList.append(n)

    return newList

def slicingList(myList:list) -> list:
    newList = myList[0:6]
    return newList



list1 = [2, 3, 4, 5, 15, 1, 43, 20]

print(f'The sum of all the items in the list is {sumList(list1)}')

print(f'The largest number in the list is : {largestNum(list1)}')

print(f'The odd numbers list from the elements of a range from 1200 to 2000 with steps of 125 is: {oddNumbers()}')
print(f'The new sliced list is: {slicingList(list1)}')
