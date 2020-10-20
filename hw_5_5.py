str_number = input('Введите числа через пробел: ')
with open('new_file.txt','w',encoding='UTF-8') as my_file:
    my_file.write(str_number)
with open('new_file.txt','r',encoding='UTF-8') as my_file:
    number_from_file = sum(list(map(int, my_file.read().split())))
    print(number_from_file)
