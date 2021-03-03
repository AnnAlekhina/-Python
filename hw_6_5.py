class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return 'Рисуем ручкой'


class Pencil(Stationery):
    def draw(self):
        return 'Рисуем карандашом'

class Handle(Stationery):
    def draw(self):
        return 'Рисуем маркером'


obj1 = Pen('Ручка')
print(obj1.draw())
obj2 = Pencil('Карандаш')
print(obj2.draw())
obj3 = Handle('Маркер')
print(obj3.draw())