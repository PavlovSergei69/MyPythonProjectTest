# #1_вариант
# class rich_uncle:
#     def __init__(self):
#         self.balance = 9999
#         self.country = 'Russia'
#
# uncle_Jonh = rich_uncle()
# print(uncle_Jonh.balance, uncle_Jonh.country, sep=',')
#
# #2_вариант
# class rich_uncle:
#     def __init__(self, balance, name):
#         self.balance = balance                            #изменили работу функции в классе
#         self.country = 'Russia'
#         self.name = name
#
# uncle_Jonh = rich_uncle(1000, 'Sergei')                            #теперь данные передаются отсюда
# print(uncle_Jonh.balance, uncle_Jonh.country, uncle_Jonh.name, sep=',')

# #3_вариант
# class rich_uncle:
#     def __init__(self, name):
#         self.name = name
#     def get_private_plane(self):
#             print(f'Сэр,{self.name}, ваш самолет ждет вас')
# uncle_Jonh = rich_uncle('Sergei')
# uncle_Jonh.get_private_plane()

#4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет.")
    def have_birthday(self):
        self.age += 1 # Увеличиваем возраст на 1
        print(f"С днём рождения, {self.name}! Тебе теперь {self.age} лет.")

person1 = Person("Алиса", 25)                     # Создаем объект
person1.introduce()
person1.have_birthday()                                     # Человек отмечает день рождения