# a = 5
# while a > 0:
#     a = a - 1
#     print ('a все еще меньше нуля')
#
# b = 5
# count = 0
# while b > 0:
#     count = count+1
#     print(f'Попытка №{count}')
#     print('b все еще больше 0')
#     if count == 2:
#         break                         #останавливает работу
#         #continue                      #продолжает работу
#
# c = 5
# count = 0
# while b > 0:
#     count = count+1
#     print(f'Попытка №{count}')
#     print('b все еще больше 0')
#     if count == 5:
#         print(f'Уже попытка №{count}, пора остановиться')
#         break

#FOR
# for i in range(12):             #будет произведен перебор чисел до 12
#     print(i**2)
# else:
#     print('В консоль выведены квадраты всех заявленных чисел')


# for k in range(12):             #будет произведен перебор чисел до 12
#     l=k**2
#     print(l)
#     if l > 100:
#         break
# else:
#     print('В консоль выведены квадраты всех заявленных чисел')

fruits = ['яблоко','огурец','банан','киви']
vegetables = ['огурец','помидор','редиска']

for fruit in fruits:
    if fruit in vegetables:
        print('Ошибка сортировки. Овощь в корзине фруктов')
        break
    else:
        print(fruit.capitalize()) #.capitalize()-выводит значения с заглавной буквы
else:
    print('В сортировке ошибок нет')