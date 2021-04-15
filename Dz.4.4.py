list_num = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in list_num if list_num.count(el) == 1]
print(f'Начальный список: {list_num}')
print(f'Конечный список: {new_list}')