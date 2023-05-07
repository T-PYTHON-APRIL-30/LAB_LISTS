main_list=[2, 3, 4, 5, 15, 1, 43, 20]

#question number 1
def sum_list(numbers:list):
    total=0
    for n in numbers:
        total+=n
    return total

print(sum_list(main_list))

#question number 2
def max_list(numbers:list):
    max_number=0
    for n in numbers:
        if n>max_number:
            max_number=n
    return max_number

print(max_list(main_list))

#question number 3
def odd_number():
    odd=[x for x in range(1200,2000,125) if x%2 !=0]
    return odd
print(odd_number())

#question number 4
new_list=main_list[4:]
print(new_list)
