# 1_вариант
# def uppercase(func):
#     def wrapper():
#         return (func().upper())
#     return wrapper
#
# def braces(func):
#     def wrapper():
#         return '{'+func()+'}'
#     return wrapper
#
# def square_braces(func):
#     def wrapper():
#         return '['+func()+']'
#     return wrapper
#
#
# @braces
# @uppercase
# @square_braces
# def great():
#     return "Hello"
#
# print(great())

# #2_вариант
# def my_decorator(func):
#     def wrapper():
#         print("До вызова функции")
#         func()
#         print("После вызова функции")
#     return wrapper
#
# @my_decorator             # Применяем декоратор к функции

# def say_hello():
#     print("Привет!")
# # Вызываем функцию
# say_hello()

#3_вариант
# def my_decorator(func):
#     def wrapper(*a, **b): # Принимаем любые аргументы
#         print("До вызова функции")
#         result = func(*a, **b) # Вызываем исходную функцию с аргументами
#         print("После вызова функции")
#         return result
#     return wrapper
#
# @my_decorator # Применяем декоратор к функции с аргументами
# def add(a, b):
#     return a + b
# # Вызываем функцию
# print(add(3, 4))

# #4_вариант
# class MyClass:
#     @staticmethod
#     def say_hello():
#         print("Привет!")
#     # Вызываем статический метод без создания экземпляра
# MyClass.say_hello()

#5_вариант
class MyClass:
    counter = 0

    @classmethod
    def increment_counter(cls):
        cls.counter += 1
        print(f"Счетчик: {cls.counter}")
# Вызываем метод класса
MyClass.increment_counter()