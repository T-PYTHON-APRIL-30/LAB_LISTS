# LAB_LISTS
my_list=[2, 3, 4, 5, 15, 1, 43, 20]

### Q1: Write a function that takes a list as a parameter, 
#and then returns  the sum  of all the items in that list.
def addition(list):
    result=0
    for element in my_list:
        result+= element
    print(result)

addition(my_list)

### Q2: Write a function that takes a list as a parameter, 
#and then returns the largest number from a list of numbers.
def largest(list):
    largest=0
    for element in my_list:
     if largest<element:
           largest= element
    print(largest)
largest(my_list)

### Q3: Create an odd numbers list from the elements of a range 
#from 1200 to 2000 with steps of 125, using [ list comprehension ].
#second_list=[*range(1200,2001)] #the * sympol unpacks the range function inside the list
oddlist = [number for number in range(1200,2000,125) if number%2 !=0]
print(oddlist)

### Q4: use list slicing to get a new list from the previous 
#list starting from the start to the 5th element in the list.
fifth_element_list=oddlist[:4]
print(fifth_element_list)

#Bonus
## Movie Ratings Analysis

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
for j in range(0,len(movies)):
    i=[number for number in movies[j][2]]
    avrage=round(sum(i)/len(i),2)
    name,date=movies[j][0:2]
    if avrage>6:
        print(f"{j+1}. {name} ({date}) - Avergae rating: {avrage} *")
