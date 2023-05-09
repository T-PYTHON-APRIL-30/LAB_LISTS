

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

# 1. Accepts a list of movies, with each movie represented as a tuple containing the movie title,
# release year, and a list of user ratings.
# 2. Calculates the average rating for each movie.
def find_average(num:list):
    average= sum(num)/len(num)
    
    return round(average,2)

new_movies_list=[]
for movie , year, rate in movies:
    if find_average(rate) > 6:
        print(f"{movie} , ({year}) - Avergae rating:{find_average(rate)} ★")
print("")


# 3. Filters out movies with an average rating lower than 6.0.
# 5. Displays the  movies, along with their title, release year, and average rating.