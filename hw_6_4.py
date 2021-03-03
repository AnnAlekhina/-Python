from time import sleep


class Car:
    def __init__(self, speed: int, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Поооехали! Юююююху!'

    def stop(self):
        return 'Погоняли и хватит'

    def turn(self, direction):
        return f'А теперь повернем {direction}'

    def show_speed(self):
        return f'Текущая скорость автомобиля  {self.speed}'


class TownCar(Car):
    def show_speed(self):
        rez = super().show_speed()
        if self.speed > 60:
            rez = f'{rez}\nНарушаем, Голубчик'
        return rez


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_sport_car = True

    def check_speed(self, speed_other_car, name_other_car):
        if self.speed > speed_other_car:
            return f'Поздравляю, вы обогнали {name_other_car} на {self.speed - speed_other_car} км/ч  '
        return f'ХА, какая-то {name_other_car} обогнала спортивную тачку на {speed_other_car - self.speed} км/ч'


class WorkCar(Car):
    def show_speed(self):
        rez = super().show_speed()
        if self.speed > 40:
            return f"{rez}\nНарушаем, Голубчик"
        return rez


class PoliceCar(Car):

    def check_speed(self, speed_other_car, car_odj, car_name):
        if (speed_other_car > 60 and isinstance(car_odj, TownCar)) or (
                speed_other_car > 40 and isinstance(car_odj, WorkCar)):
            if self.speed >= speed_other_car:
                return f'я догнал {car_name} и оштрафовал. '
            return f'Нарушитель  {car_name} оказался слишком шустрым'
        elif isinstance(car_odj, SportCar):
            sleep(1)
            return f'Все равно не догоню спортивную {car_name}, даже не буд пытаться проверить скорость'
        else:
            return f'{car_name} едет с допустимой скоростью'


name = input('Введите марку машины: ')
car1 = Car(40, 'Желтая', name, False)
print(car1.go())
direcrion = input('Куда повернем? ')
print(car1.turn(direcrion))
print(car1.show_speed())
print(car1.stop())
name = input('Введите марку машины: ')
speed = int(input(f'С какой скоростью поедет {name} TownCar: '))
car2 = TownCar(speed, 'Cиняя', name, False)
print(car2.show_speed())
name = input('Введите марку машины: ')
speed = int(input(f'С какой скоростью поедет {name} SportCar: '))
car3 = SportCar(speed, 'Красная', name, False)
print(car3.check_speed(car1.speed, car1.name))
speed = int(input('С какой скоростью поедет Полицейская Машина?: '))
car4 = PoliceCar(speed, 'Белая', 'какая-то мусорская', True)
print(car4.check_speed(car2.speed, car2, car2.name))
print(car4.check_speed(car3.speed, car3, car3.name))

