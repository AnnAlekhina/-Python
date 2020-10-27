class Cell:
    def __init__(self,n):
        self.n = n

    def __add__(self, other):
        return '*' * (self.n + other.n)

    def __sub__(self, other):
        if self.n == other.n:
            return 'Количество ячеек в клетах одинаковое'
        else:
            return '*' * abs(self.n - other.n)

    def __mul__(self, other):
        return '*' * (self.n * other.n)

    def __truediv__(self, other):
        try:
            rez = self.n / other.n
            if int(rez) > 0:
                return '*' * int(rez)
            else:
                return 'Резудьтат деления равен 0'
        except ZeroDivisionError as err:
            return f'количество ячеек в одной из клеток равно 0 {err}'

    def make_order(self,n_el):
        rez =''
        rez_div, ost = divmod(self.n,n_el)
        for i in range(rez_div):
            rez += f'{n_el * "*"}\n'
        rez += f'{ost * "*"}'
        return rez







el = Cell(2)
el_2 = Cell(4)
el_3 = Cell(15)
print(el+el_2)
print('----------------')
print(el-el_2)
print('----------------')
print(el*el_2)
print('----------------')
print(el_3/el_2)
print('----------------')
print(el_3.make_order(4))