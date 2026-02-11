#1.1_вариант
number = lambda a,b: a-b            #анонимные, простые и быстрые функции
print(number(49,54))

#1.2_вариант
number = lambda a,b: a+b
result = number(55,11)
print(f'Сумма числе равна {result}')

#2.1_вариант сортировка
numbers = [1,5,7,-10,15,-45,92]
result_sorted = sorted(numbers,key = lambda x: abs(x))      #sorted-сортировка. ABS-модуль числа
print(result_sorted)

#2.1_вариант сортировка
numbers = [1,5,7,-10,15,-45,92]
result_sorted = sorted(numbers)      #sorted-сортировка. Просто сортировка от меньшег ок большему
print(result_sorted)

#3_вариант. Функция map() применяется для всех элементов списка, выполняя операцию, указанную в лямбда-функции.
numbers = [1, 2, 3, 4, 5,6,7]
squared_numbers = list(map( lambda x: x ** 3, numbers))
print(squared_numbers)

#4_вариант. Функция filter() используется для фильтрации элементов, которые удовлетворяют условию, заданному в лямбда-функции.
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#5_вариант. Функция sorted() может сортировать элементы с использованием лямбда-функции,которая указывает, как сравнивать элементы.
students = [('Alice', 25), ('Bob', 30), ('Charlie', 20)]
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)