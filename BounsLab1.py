list_of_movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
]
def movies(list_of_movies:list):
 for elem in list_of_movies:
    s= sum(elem[2])
    l = len(elem[2])
    result = s //l
    if result >6:
       print(f"{elem[0]}. ({elem[1]}) - Average rating: {float(result)} ★")
       #print(f"{elem[0]}. ({elem[1]}) - Average rating: {round(result,2)} ★")
movies(list_of_movies)
