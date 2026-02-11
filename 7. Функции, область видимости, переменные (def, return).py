#1_вариант
def calculate(a,b):
    return(a+b)

result_1 = calculate(5, 6)
result_2 = calculate(55, 449)
print(result_1,result_2, sep='|')

#2_вариант
def calculate(a,b):
    return(a+b)
result_1 = calculate(15, 60)
result_2 = calculate(55, 449)
print(result_1,result_2, sep='|')

#3_вариант
def greet(second_name):
    print(f"Привет, {second_name}!")
greet("Павлов")

4_вариант
def square(number):
    return number * number
result=square(11)                   #в даннмоу случаем result является переменной, где я ввоже число
print(f'Квадрат числа:', {result})

#5_вариант
def greet(name="чевлоек, который не ввел данные"):
    print(f"Привет, {name}!")
greet() #Привет, гость!
greet("Анна") # Привет, Анна!

#6_вариант
s=lambda x:x+150
print(s(10))

#7_вариант
def greet():
    print('обро п')
greet()

#8_вариант
def calculate(a,b):
   return(a+b)

result = calculate(5, 6)
print(f'Сумма числе равно {result}')
# print(f'Сумма чисел равна {calculate(5, 6)}')  #можно написать одной строкой


#9_вариант
def my_function(local_var):
    local_var = 10 # Локальная переменная
    print(f"Локальная переменная: {local_var}")
my_function()
# print(local_var) # Ошибка: переменная вне функции недоступна



