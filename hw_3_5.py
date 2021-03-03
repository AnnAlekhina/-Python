def cheak_exit(str_numbers):
    if list(str_numbers[-1])[-1].lower() == 'q':
        return True


def sum_numbers(list_numbers):
    global rez
    rez += sum(list_numbers)
    return rez


def cheak_space(str_numbers):
    if str_numbers[-1] == '':
        str_numbers = str_numbers[:-1]
        return str_numbers
    else:
        return str_numbers


rez = 0
while True:
    numbers = input('Введите строку чисел (если хотите завершить программу, введите q) : ').split(' ')
    numbers = cheak_space(numbers)
    if cheak_exit(numbers) != True:
        new_list_number = list(map(int, numbers))
    else:
        new_list_number = list(map(int, numbers[:-1]))
        break

    print(sum_numbers(new_list_number))
print(f'Программа завершена, результат суммирование {sum_numbers(new_list_number)}')