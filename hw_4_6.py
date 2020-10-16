from itertools import count, cycle
from time import sleep

print('------------Пункт А------------------')
start_number = int(input('Введите стартовое число: '))
stop_number = int(input('Введите последнее число: '))

new_number_gen = (el for el in count(start_number))
for el in new_number_gen:
    if el <= stop_number:
        sleep(0.5)
        print(el)
    else:
        sleep(0.5)
        break

print('------------Пункт Б------------------')
new_list = input('Введите числа через пробел: ')
length = int(input('Введите длину последовательности: '))
new_list = new_list.split(' ')
i = 0

new_list_gen = (el for el in cycle(new_list))
for el in new_list_gen:
    if i < length:
        sleep(0.5)
        i += 1
        print(el)
    else:
        sleep(0.5)
        print('конец последовательности')
        break





