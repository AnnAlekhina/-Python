from sys import argv


script_name, work_hour, rate, prize = argv


def salary_func(work_hour,rate,prize):
    return (int(work_hour)*int(rate))+int(prize)


print(f'Зарплата сотрудника составляет {salary_func(*argv[1:])} рублей в месяц')

