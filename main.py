# ----------- Lists Lab -----------
print("---------- Lists Lab ----------")

numList = [2, 3, 4, 5, 15, 1, 43, 20]
print("----- Q1 -----")
def numSum (numbers):
    total = 0 
    for num in numbers:
        total+=num
    return total # also you can write ( sum(numbers) )
print("The total sum is:",numSum(numList))

print("----- Q2 -----")
def maxNum (numbers):
    return max(numbers)
print("The max number in the list is:",maxNum(numList))

print("----- Q3 -----")
def oddNum(num1 : int , num2 : int):
    return [numbers for numbers in range(num1,num2,125) if numbers%2 != 0]

number1 , number2 = 1200 , 2000
print("The odd numbers in the list are: {}".format(oddNum(number1,number2)))

print("----- Q4 -----")
def slicNum (numbers):
    return numbers[:5]
print("The numbers from index 0 to 5 are: ",slicNum(numList))