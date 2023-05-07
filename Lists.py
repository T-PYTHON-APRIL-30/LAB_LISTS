main_list = [2, 3, 4, 5, 15, 1, 43, 20]
def Sum (List):
    print(sum(main_list))

Sum(main_list)
#__________________________________________

def max_number (List):
    print (max(main_list))

max_number(main_list)
#__________________________________________

comper_list = [x for x in range(1200,2000,125) if x%2 != 0]
print (comper_list)
#__________________________________________

new_list = main_list[:5]
print (new_list)