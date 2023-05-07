myList = [2,3,4,5,15,43,20]

def listSum(givenList :  list):
    number = sum(givenList)
    return number

print(listSum(myList))

def largestNumInList(givenList : list):
    givenList.sort()
    return givenList[-1]

print(largestNumInList(myList))

oddList = [x for x in range(1200,4000,125) if x%2 != 0]
print(oddList)

slicedList = oddList[:5]
print(slicedList)


moviesList = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

def getAVG(x,y):
    summ = sum(moviesList[x][y])
    avg = summ/len(moviesList[x][y])
    return avg

def displayL(givenList : list):
    number = 0
    for element in moviesList:
        
        avg = getAVG(number,2)
        if filterR(avg):
            (print(f"{number+1}, {moviesList[number][0]}, ({moviesList[number][1]}), - Average Rating: {round(avg,2)} ★ "))
            
            number += 1
            
           # moviesList.sort() , only shows the top four without the last one

def filterR(number):
    if number >= 6:
        return True
    else:
        return False

#listN = moviesList.sort(reverse=True)
#newN = moviesList.sort()
displayL(moviesList)