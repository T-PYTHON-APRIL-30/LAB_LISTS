
# list of movies with their details
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

# list to store the movies with their average rating
movies_with_rating = []

# calculate the average rating for each movie and filter out the movies with a rating less than 6.0
for movie in movies:
    title, year, ratings = movie
    avg_rating = sum(ratings) / len(ratings)
    if avg_rating >= 6.0:
        movies_with_rating.append((title, year, avg_rating))

# sort the movies by their average rating in descending order
movies_with_rating.sort(key=lambda x: x[2], reverse=True)

# display the movies with their details and average rating
for i, movie in enumerate(movies_with_rating):
    title, year, avg_rating = movie
    print(f"{i+1}. {title} ({year}) - Average rating: {avg_rating:.2f} ★")
