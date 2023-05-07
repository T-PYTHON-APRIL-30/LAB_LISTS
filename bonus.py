'''Movie Ratings Analysis
Scenario: You have just been hired as a data analyst at a movie streaming platform. Your manager has given you a list of movies, each with a tuple containing the movie title, release year, and user ratings. The platform allows users to rate movies on a scale of 1 to 10. Your manager wants you to create a Python program that:

Accepts a list of movies, with each movie represented as a tuple containing the movie title, release year, and a list of user ratings.
Calculates the average rating for each movie.
Filters out movies with an average rating lower than 6.0.
Displays the movies, along with their title, release year, and average rating.'''

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

def find_average(numbers :list):
    average = sum(numbers)/len(numbers)
    return round(average,2)


print("")
new_list = []
place = 0
for movie , year, rate ,in movies:
    if find_average(rate) > 6:
        place += 1
        print(f"{place}. {movie} ({year}) - Average rating: {find_average(rate)} ★")
print("")



