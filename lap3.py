'''Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.
Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].
Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
Bonus
Movie Ratings Analysis
Scenario: You have just been hired as a data analyst at a movie streaming platform. Your manager has given you a list of movies, each with a tuple containing the movie title, release year, and user ratings. The platform allows users to rate movies on a scale of 1 to 10. Your manager wants you to create a Python program that:

Accepts a list of movies, with each movie represented as a tuple containing the movie title, release year, and a list of user ratings.
Calculates the average rating for each movie.
Filters out movies with an average rating lower than 6.0.
Displays the movies, along with their title, release year, and average rating.
Example input:

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
Expected output:

1. The Shawshank Redemption (1994) - Avergae rating: 9.17 ★
2. The Godfather (1972) - Avergae rating: 8.83 ★
3. The Dark Knight (2008) - Avergae rating: 8.83 ★
4. Schindler's List (1993) - Avergae rating: 7.83 ★
5. Pulp Fiction (1994) - Avergae rating: 7.17 ★'''
#Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.
myList=[2, 3, 4, 5, 15, 1, 43, 20]
def sumOfPar(myList=[]):
    sum=''
    for i in myList:
        sum+=i
    return sum
sumOfPar()
print(sum)
#Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
def LargOfPar(myList=[]):
    num=''
    for i in myList:
        if i>num:
            largestNum=i
    return num
LargOfPar()
print(f"the largest number is :"{largestNum})
#Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].
listComp=[1200:2000:125]
def AnOddNum(oddNum:int):
    for n in range(1200,2000):
        if n%2!=0
        oddNum =n
        return oddNum
AnOddNum(oddNum)
#Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
print("my slicing list is:")
i=0
for i in myList:
    print(myList[:4]," ")

