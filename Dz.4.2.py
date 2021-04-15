list_num = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(list_num)
new_list = [list_num[el] for el in range(1, len(list_num)) if list_num[el - 1] < list_num[el]]
print(new_list)