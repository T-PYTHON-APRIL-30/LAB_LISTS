
# Write a function that takes a list as a parameter,
# and then returns the sum of all the items in that list.
total = 0
# creating a list
list_number = [12, 3, 4, 5, 15, 1, 43, 20]
#add them in variable total
for elements in range(0, len(list_number)):
	    total = total + list_number[elements]
# printing total value
print("Sum of all elements in given list: ",total)

print("--"*14)

#Write a function that takes a list as a parameter,
#and then returns the largest number from a list of numbers.
list_number.sort()
 
# printing the last element
print("Largest element is:", list_number[-1])

print("--"*14)
#list comphersion

new_list = [value for value in range(1200,2000,125)] 
print(new_list)

print("--"*14)

print(new_list[:5])












