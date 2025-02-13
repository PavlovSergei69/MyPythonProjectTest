# print_hi('Sergei')
number = 100  #integer
float_number = 16.5  #float
text = 'Цитата: "А внутри другая цитата"'  #string
another_text = 'Еще одна цитата'  #string
bolean_value = True  #boolean
another_bolean_value = False  #boolean

a, b, c = 10, 15, 25  #переменные вложеннеы в одну строку
print(a)  #выдает значение 10

values = [1, 'число', 43, 99] #List (список), он фиксируется в [квадратные] скобки, а кортеж в (круглые)
print(values[1], type(values))                   #выведет второе число. Отсчет начинается с 0. В данном варианте будет 'число'

dictionary = {"car": "машина", "dog": "собака", "cat": "кошка"}     #Dictionaries (словари)
print(dictionary["car"])           #выведет значение "машина".
user = {
"name": "Alice",
"age": 25,
"is_admin": False
}
print(user["name"], type(user))

print(number, float_number, bolean_value, sep=',') #Sep (разделитель) разделяет значение определенным знаком, который задан разработчико

unique_numbers = {1, 2, 3, 3, 4, 4, 5} #Set (множества) хранят и выводят уникальный данные, дубликаты удаляют.
print(unique_numbers, type(unique_numbers))

