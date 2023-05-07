movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

def average_rating(rates: list) -> float:
    avg: float = 0.0
    for rate in rates:
        avg = sum(rates)/len(rates)
    return round(avg, 2)


def movie_filter(avg: float) -> bool:
        if avg > 6.0:
            return True
        else:
            return False


i: int = 0
new_movies = []
for element in movies:
    avg: float = average_rating(movies[i][2])
    if movie_filter(avg) == True:
        item = f"{movies[i][0]} ({movies[i][1]}) - Avergae rating: {avg} ★"
        new_movies.append([avg, item])
    i += 1


new_movies.sort(reverse = True)
j: int = 0
for element in new_movies:
    print(f"{j + 1}. {new_movies[j][1]}")
    j += 1