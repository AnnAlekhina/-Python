from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def cloth_consumption(self):
        pass

class Coat(Clothes):
    def __init__(self,size):
        self.size = size


    @property
    def cloth_consumption(self):
        return f'{self.size/6.5 + 0.5}\nЗаписалось'

    
class Suit(Clothes):
    def __init__(self,height):
        self.height = height

    @property
    def cloth_consumption(self):
        return f'{2*self.height + 0.3}\nЗаписалось'


el_1 = Coat(42)
el_2 = Suit(100)
print(el_1.cloth_consumption)
print(el_2.cloth_consumption)
