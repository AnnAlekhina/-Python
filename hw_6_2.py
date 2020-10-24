class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_road(self, mass, depth):
        return mass*(depth/1000)*self._length*self._width


my_road = Road(length=5000, width=20)
rez = my_road.mass_road(mass=25, depth=5)
print(f'Необходимо {rez} тонн асфальта')