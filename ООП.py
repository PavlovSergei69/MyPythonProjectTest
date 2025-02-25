from abc import ABC
class car(ABC):
    def __init__(self):
        self.hp = 250
    def drive(self):
        pass                            #!!!пустота!!! необходима для заполнения, коогда нет больше данных
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
niva_legend = niva()
niva_legend.drive()
niva_legend.stop()
niva_legend.lights()
