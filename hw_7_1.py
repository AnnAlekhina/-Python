class Matrix:
    def __init__(self,matr):
        self.matr = matr

    def __str__(self):
        new_matr = ''
        buf2 = list(map(str, self.matr))
        for i in range(len(self.matr)):
            buf = ' '.join(buf2[i].split(','))

            new_matr += f'{buf[1:-1]}\n'
        return new_matr

    def __add__(self, other):
        try:
            new_matr = []
            rez_matr = []
            for i in range(len(self.matr)):
                new_matr.clear()
                for j in range(len(self.matr[0])):
                    rez = self.matr[i][j] + other.matr[i][j]
                    new_matr.append(rez)
                    rez_matr.append(new_matr[:])
            return Matrix(rez_matr)
        except IndexError as err:
            return f'Матрицы должны быть одного размера!! {err}'


m = Matrix([[1, 2, 3], [4, 5, 6], [1, 1, 1]])
m2 = Matrix([[1, 2, 3], [4, 5, 6]])
rez = m+m2
print(rez)