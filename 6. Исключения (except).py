# #Вариант 1
# try:
#     a = '10ac'
#     print(int(a))
# except ValueError as e:
#     print('Получена ошибка ValueError:',e.args)

# #Вариант 2
# try:
#      a = '10ac'
#      c = 10 / 0
#      print(int(a))
# except ZeroDivisionError as e:
#      print('Получена ошибка ZeroDivisionError:', e.args)  #В данном случае выпадает только вторая ошибка

# #Вариант 3
# try:
#     a = '10ac'
#     print(int(a))
#     c = 10 / 0
# except (ValueError, ZeroDivisionError)  as e:
#     print('Получена ошибка:',e.args)                #В данном случае выпадает только первая ошибка
#
#Вариант 4.1
# try:
#     a = '10ac'
#     # c: float = 10/0
#     # print(int(a))
# except  ValueError as e:
#     print('Получена ошибка:',e.args)
# except  ZeroDivisionError as e:
#     print('Получена ошибка:',e.args)
# else:
#     print('Исключение не появилось, код работает отлично')
# finally:
#     print('Я блок, который выполняется всегда')

# Вариант 4.2
# try:
#     result = 10 / 0
# except ZeroDivisionError :
#     print("Ошибка деления на ноль.")
# else:
#     print("Результат:", result) # Выполнится, если ошибок не было
# finally:
#     print("Завершение программы.") # Выполнится в любом случае


# #Вариант 4.3
# try:
#     a = '10ac'
#     c: float = 10/0
#     print(int(a))
# except  ValueError as e:
#     print('Получена ошибка:',e.args)
# except  ZeroDivisionError as e:
#     print('Получена ошибка:',e.args)

#Дополнительно
while True:
     try:
          number = int(input("Введите число: "))
          print(f"Вы ввели число: {number}")
          break # Выход из цикла, если ошибок нет
     except ValueError:
          print("Это не число! Попробуйте снова.")