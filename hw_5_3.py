from functools import reduce


def sum_func(prev_el, el):
    return prev_el + el


with open('test_5_3.txt') as my_file:
    content = my_file.readlines()

new_content = []
for string in content:
    new_content.append(string.split())
new_content = list(zip(*new_content))
for i in range(len(new_content[0])):
    if int(new_content[1][i]) < 20000:
        print(f'Сотрудник {new_content[0][i]} зарабатывает менее 20 т.р')
rez = reduce(sum_func, map(int,new_content[1]))/len(new_content[0])
print(f'Средний доход сотрудников составляет: {rez} рублей')
