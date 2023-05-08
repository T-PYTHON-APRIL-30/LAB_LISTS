#given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
#Q1: Write a function that takes a list 
#as a parameter, and then returns the sum of all the items in that list.

sum_list = [ 2, 3, 4, 5, 15, 1, 43, 20]
total_sum = sum_list(sum_list)
print (sum_list(list))


#Write a function that takes a list as a parameter,
#and then returns the largest number from a list of numbers.

#list of numbers 
list = [2, 3, 4, 5, 15, 1, 43, 20] 
list.sort()
print("largest element is :", list [])


#Create an odd numbers list f
# rom the elements of a range from 1200 to 2000 with steps of 125, 
# using [ list comprehension ].

odd_numbers_list = [num for num in range(1200, 2000, 125) 
if sum % 2 != 0]
print(odd_numbers_list)

#use list slicing to get a new list from the previous list starting from 
# the start to the 5th element in the list.


new_list = [ 2, 3, 4, 5, 15]




#bouns
#Scenario: You have just been hired as a data analyst at a movie streaming platform.
#  Your manager has given you a list of movies, each with a tuple containing the movie title, release year, 
# and user ratings. The platform allows users to rate movies on a scale of 1 to 10.
#  Your manager wants you to create a Python program that:

#1-Accepts a list of movies, with each movie represented as a tuple containing the movie title, release year, 
# and a list of user ratings.

movies_watch =[("The Shawshank Redemption", 1994, [9, 10, 8, 9, 10]),
                ("The godfather", 1972, [10, 9, 10, 8, 9]),
                (T"he Dark Knight", 2008 [9, 10, 9, 8, 7]),
                ("Pulp Fiction"),1994 [8, 7, 9, 10])]

#calculate the average rating for each movies
avg_rating =[]
for movies in movies:
    title = movies[0]
    year = movies[1]
    rating = movies[2]
    avg_rating = sum(rating)/len(rating)
    avg_rating.append(title, year, avg_rating))

    #sort the movies based on their averge rating in descending order

    sorted_movies = sorted(avg_rating, key=lambda x: x[2], reverse=True)

    #print out the soted list of movies with their average raitng:

    for movies in sorted_movies:
        print (f"{movies[0]}({movies [1]}){movies[2]:.1f}")


#3-Calculates the average rating for each movie.

movies = [("The Shawshank Redemption", 1994, [9, 10, 8, 9, 10]),
                ("The godfather", 1972, [10, 9, 10, 8, 9]),
                (T"he Dark Knight", 2008 [9, 10, 9, 8, 7])]

for movie in movies
title = movies[0]
rating = movie[2]
avg_rating = sum(rating)/len(rating)
print(f"{title}:{average_rating:.2f}")


#4-ilters out movies with an average rating lower than 6.0.

movies = [("The Shawshank Redemption", 1994, [9, 10, 8, 9, 10]),
                ("The godfather", 1972, [10, 9, 10, 8, 9]),
                (T"he Dark Knight", 2008 [9, 10, 9, 8, 7])]

filterd_movies = []
for movie in movies:
    title = [0]
    year = movie[1]
    rating = movie[2]
    avg_rating = sum(rating)/len(rating)
    if avg_rating>= 6.0:
        filterd_movies.append((title, year))
    print(filterd_movies)

    #5isplays the movies, along with their title, release year, and average rating.
movies = [("The Shawshank Redemption", 1994, [9, 10, 8, 9, 10]),
                ("The godfather", 1972, [10, 9, 10, 8, 9]),
                ("The Dark Knight", 2008 [9, 10, 9, 8, 7])
                ("12 Angry Men", 1957, [9, 8, 10])
                ("Schindler's List", 1993, [ 10, 9])

                for movie in movies:
                title = movie[0]
                year = [1]
                rating = [2]
                
                avg_rating = sum(ratings)/len(ratings)

                print_f"{title}({year}):{avg_rating}")