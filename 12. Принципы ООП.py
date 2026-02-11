#Абстракция
from abc import ABC

class car(ABC):
    def __init__(self):
        pass                         #Мощность машины

    def power(self):
        pass
    def drive(self):
        pass                            #!!!пустота!!! Необходима для заполнения, когда нет больше данных, но функцию или класс нужно закрыть.
    def stop(self):
        pass
    def lights(self):
        pass

class niva(car):
    def drive(self):
        print('Едем')

    def stop(self):
        print('Тормозим')

    def lights(self):
        print('Светим')

    def power (self):
        self.power = 250
        print(f'Мощность автомобиля {self.power}')

niva_legend = niva()
niva_legend.drive()
niva_legend.stop()
niva_legend.lights()
niva_legend.power()


#проверка введения веток