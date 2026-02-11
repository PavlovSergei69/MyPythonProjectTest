# #1_вариант
# def add_all(*args):             # Мы работаем c кортежем
#     all_summary = 0
#     for num in args:
#         all_summary = all_summary + num      # all_summary += num
#     return all_summary
# values = [1,2,3,4,5,6]
# more_values = [10,20,30,40,50,60]
# print(add_all(*values))             #"*" здесь используется тк в 2 строке *args является кортежем(неизменяемым списком).
#                                     # Поэтому для отображения обычного списка используется *values
# print(add_all(*values,*more_values))

# #1.2_вариант
# def print_numbers(*args):
#     for num in args:
#         print(num)
# print_numbers(1, 2, 3, 4, 5)

# #2_вариант
# def autorize(**kwargs): # Мы работаем c словарем
#
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#
# autorize(name='Sergey', age='29', job='QA')

# #3_вариант
# def autorize(**kwargs):
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#
# date = {'Name:': 'Sergey', 'Age:': '28', 'Job:': 'QA'}
# autorize(**date)

# #3.1_вариант
# def print_user_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_user_info(name="John", age=30, city="New York")

#4.1_вариант. Применение *args и **kwargs

def print_details(name, *args, **kwargs):
    print(f"Name: {name}")
    print("Other details:")
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_details("Alice", 25, "Engineer", city="London", country="UK")


#4.2_вариант. Применение *args и **kwargs
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
args = ["John", 25]
greet(*args)

# Мы можем комбинировать их в одной функции, но *args всегда идет первым, а`kwargs` после**.


