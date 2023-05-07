#print the sum of list
my_list = [2,3,4,5,15,1,43,20]

def sum_numbers(new_list:list):
    sum = 0

    for n in new_list:
       sum += n

    return sum
    
print("The sum of list is:",sum_numbers(my_list))

#print the largest number    
def largest_number(largest_list:list):
    numbers = 0

    for a in largest_list:
        if a > numbers:
            numbers = a

    return numbers
    
print("The largest number is:",largest_number(my_list))

#print odd numbers
odd_numbers = [count for count in range(1200,2000,125) if count % 2 != 0]
print("Odd numbers:",odd_numbers)

#used slicing
slicing_list = my_list[:5]
print(slicing_list)