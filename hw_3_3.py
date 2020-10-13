def two_max(list_num):
    list_num.sort()
    return list_num[1]+list_num[2]


numbers = (input('Введите три числа через пробел: ').split(' '))
new_list_numbers = list(map(int, numbers))
print(two_max(new_list_numbers))

