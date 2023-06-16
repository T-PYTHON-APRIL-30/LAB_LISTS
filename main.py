movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]


sum =0
count =0
length= len(movies)
movies_rating= []


index_number=0
while index_number <= length-1:

    for number in movies[index_number][2][:]:
        sum +=number
        count+=1
    average =round(sum/6,2)
    movies_rating.append(average)
    index_number+=1
    sum=0
    count=0

n=0
for element in movies:
    if movies_rating[n] > 6.0:
        print(f"{movies[n][0]} ({movies[n][1]}) - Average rating: {movies_rating[n]} ★")
    n+=1
    my_list =[2,3,4,5,15,1,43,20]

def sum_of_items(list1 :list ) ->int:
    sum = 0
    for element in list1:
        sum +=element
    return sum 

print(f"The sum of items is: {sum_of_items(my_list)}")

def largest_number(list2 : list) -> int:
    max_number = 0
    for element in my_list:
        if element > max_number:
            max_number = element
    return max_number

print(f"The largest number is: {largest_number(my_list)}")

odd_numbers_list= [number for number in range(1200,2000,125) if number%2 != 0]

print(f"The list with odd numbers: {odd_numbers_list}")

new_list = my_list[:5]

print(f"The new list: {new_list}")