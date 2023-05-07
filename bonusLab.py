'''Movie Ratings Analysis
Scenario: You have just been hired as a data analyst at a movie streaming platform. Your manager has given you a list of movies,
 each with a tuple containing the movie title, release year, and user ratings. The platform allows users to rate movies on a scale
   of 1 to 10. Your manager wants you to create a Python program that:

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




def ratingAvg(myList:list) -> float:
    sum = 0
    counter = 0

    for i in range (0,len(myList)-1):
        for j in range (0,i-1):
            sum += [i][j-1]
            counter +=1

    average = sum/counter

    return round(average)

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])]

movieRateList = []

for n in range (0,len(movies)-1):
    movieRateList.append(movies[n][2])


#print(ratingAvg(movieRateList))

print(movieRateList)

print(f'The average is {ratingAvg(movieRateList)}')

'''for n in range (0,len(movies)-1):
    print(f'The average rate for {movies[n][0]} is {ratingAvg(movieRateList)}')
#print(ratingAvg(movieRateList))'''
