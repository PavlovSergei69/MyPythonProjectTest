number = 100  # integer (целое число)

float_number = 16.5  #float (число с плавающей точкой)

text_1 = 'Цитата: "А внутри другая цитата"'  # string (строка)
text_2 = 'Цитата: \'А внутри другая цитата\' ' # < \ > помогает корректно работать компиляции кода. Иначе после цитаты все схлопнется, и пойдет ошибка.
another_text = "Еще одна цитата"
print(text_1)

bolean_value = True  # boolean (булевые значения). Либо да, либо нет. Либо true, либо false.
another_bolean_value = False  # boolean


a, b, c = 10, 15, 25  # переменные вложены в одну строку
print(a)  # выдает значение 10

values = [1, 'число', 43, 99] # List (список), он фиксируется в [квадратные] скобки, а кортеж в (круглые)
print(values[1], type(values))                   # выведет второе число. Отсчет начинается с 0. В данном варианте будет 'число'

dictionary = {"car": "машина", "dog": "собака", "cat": "кошка"}     #Dictionaries (словари), частный случай списка
print(dictionary["car"])           # выведет значение "машина".
user = {
"name": "Alice",
"age": 25,
"role_is_admin": False
}

print(user["role_is_admin"], type(user))
print(user)

unique_numbers = {1, 2, 3, 3, 4, 4, 5} #Set (множества) хранят и выводят уникальный данные, дубликаты удаляют.
print(unique_numbers, type(unique_numbers))

print(number, float_number, bolean_value, sep='_разделение_') #Sep (разделитель) разделяет значение определенным знаком, который задан разработчико


