income = int(input('Введите сумму выручки фирмы: '))
costs = int(input('Введите сумму издерже фирмы: '))
if income>costs:
    profit=income-costs
    print('Фирма отработала с прибылью: ',profit)
    ren = (profit/income)*100
    print('Рентабельность фирмы составляет: ',ren,'%')
    workers = int(input('Введите количество сотрудников фирмы: '))
    profit_workers=profit/workers
    print('Прибыль в расчете на одного сотрудника составляет: ',profit_workers)


elif income==costs:
    print('Фирма отработала "в ноль"')
else:
    print('Фирма отработала с убытками')