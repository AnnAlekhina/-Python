from itertools import cycle
from time import sleep
from datetime import datetime


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self, cnt):
        i = 0
        color_dict = {1:('красный',7),2:('желтый',2),3:('зеленый',5),4:('желтый',7)}

        for el in cycle(color_dict):
            self.__color = color_dict[el][0]
            print(self.__color)
            start = datetime.now()
            sleep(color_dict[el][1])
            print(f'Светофор горел {datetime.now() - start}')
            i += 1
            if i == cnt:
                return
        return


a = TrafficLight()
a.running(7)




