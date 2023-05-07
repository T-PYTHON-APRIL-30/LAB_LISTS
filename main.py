"""
# LAB_LISTS


## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.
### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].
### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

"""
listexp=[2, 3, 4, 5, 15, 1, 43, 20]

def sumList(llist):
    sum=0
    for i in llist:
        sum+=i
    return sum

print(sumList(listexp))

def largestNumberInList(llist):
    largest = llist[0]
    for num in llist:
        if  num > largest:
            largest = num
    return largest
    
print(largestNumberInList(listexp))


oddNumber = [x for x in range(1200,2000,125) if x % 2 != 0]
print(oddNumber)

newList=listexp[:5]
print(newList)

