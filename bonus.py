movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

def average_rating(rate:list):
    total=0
    num=0
    for n in rate:
        total+=n
        num+=1
    return total/num


def Filter_rate(number):
    if number>=6:
        return True
    else:
        return False
def Display(display_list):
    i=0
    for num in display_list:
        avg=average_rating(display_list[i][2])
        if Filter_rate(avg)==True:
            print(f"{display_list[i][0]} ({display_list[i][1]}) - Avergae rating: {round(avg,2)} ★ ")
        i+=1
Display(movies)
