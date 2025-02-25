#1_вариант
number = lambda a,b: a-b            #анонимные, простые и быстрые функции
print(number(49,54))

#2_вариант сортировка
numbers = [1,5,7,-10,15,-45,92]
result_sorted = sorted(numbers,key = lambda x: abs(x))      #sorted-сортировка. ABS-модуль числа
print(result_sorted)