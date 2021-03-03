list_number = input('Введите цифры через пробел: ').split(' ')
list_number = list(map(int,list_number))
new_list = [list_number[i] for i in range(1, len(list_number)) if list_number[i] > list_number[i-1]]
print(new_list)