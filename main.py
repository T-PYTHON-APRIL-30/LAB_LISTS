'''
# LAB_LISTS


## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.
### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].
### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
'''
def sumAll(list : list) ->int:
    sum: int = 0
    for element in list:
        sum += element
    return sum
def SearchLarge(list : list) -> int :
    large : int = 0
    for element in list :
        if element > large :
            large = element

    return large

numberList : list = [2, 3, 4, 5, 15, 1, 43, 20]
print(sumAll(numberList))
print(SearchLarge(numberList))

def oddNumber() -> list:
    return [x for x in range(1200, 2000, 125) if x%2 == 1]

print(oddNumber())
print(numberList[:5])

'''

# Bonus

## Movie Ratings Analysis

Scenario:
You have just been hired as a data analyst at a movie streaming platform. Your manager has given you a list of movies, each with a tuple containing the movie title, release year, and user ratings. The platform allows users to rate movies on a scale of 1 to 10. Your manager wants you to create a Python program that:

1. Accepts a list of movies, with each movie represented as a tuple containing the movie title, release year, and a list of user ratings.
2. Calculates the average rating for each movie.
3. Filters out movies with an average rating lower than 6.0.
5. Displays the  movies, along with their title, release year, and average rating.

Example input:
```
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
```

Expected output:
```
1. The Shawshank Redemption (1994) - Avergae rating: 9.17 ★
2. The Godfather (1972) - Avergae rating: 8.83 ★
3. The Dark Knight (2008) - Avergae rating: 8.83 ★
4. Schindler's List (1993) - Avergae rating: 7.83 ★
5. Pulp Fiction (1994) - Avergae rating: 7.17 ★
```

'''
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
print(movies[0][2])

def average(list : list) -> int:
    return round(sumAll(list)/len(list), 2)

def averageAll() -> list:
    averageList : list =[]
    for tuple in movies :
        averageList.append((tuple[0], average(tuple[2])))
    return averageList

print(averageAll())


def filterOut(list:list) -> list:
    return [x for x in list if x[1] >= 6]


averageList = averageAll()
filterList = filterOut(averageList)

def toString(list : list):
    count =0
    for element in list:
        for movie in movies:
            if element[0] == movie[0]:
                count +=1
                print(f"{count}. {movie[0]} ({movie[1]}) - Avergae rating: {element[1]}")
                break

toString(filterList)
