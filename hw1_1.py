var1 = 5.0
var2=5
var3='привет'
print(var1,var2,var3)
var1 = int(input('Введите первое число: '))
var2 = float(input('Введите второе число: '))
var3 = input('Введите строку: ')
print(f"вы ввели данные {var1}, {var2}, {var3},"
      f" они имеют типи соответственно: {type(var1)},{type(var2)},{type(var3)}")
