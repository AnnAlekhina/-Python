class Complex:
    def __init__(self,imz,rez):
        self.imz = imz
        self.rez = rez
    def __str__(self):
        if self.rez >= 0:
            return f'{self.imz} + {self.rez}i'
        else:
            return f'{self.imz} - {self.rez}i'

    def __add__(self, other):
        return Complex(self.imz + other.imz, self.rez + other.rez)

    def __mul__(self, other):
        return Complex(self.imz * other.imz - self.rez*other.rez, self.imz*other.rez + self.rez * other.imz)

a1,b1 = list(map(int,input('Введите действительную и мнимую части первого числа через пробел: ').split(' ')))
comp_1 = Complex(a1,b1)
a2,b2 = list(map(int,input('Введите действительную и мнимую части первого числа через пробел: ').split(' ')))
comp_2 = Complex(a2,b2)
print(comp_1 + comp_2)
print(comp_1 * comp_2)
