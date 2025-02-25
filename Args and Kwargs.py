# #1_вариант
# def add_all(*args):             #работа с кортежем
#     all_summary = 0
#     for num in args:
#         all_summary += num      #all_summary = all_summary + num
#     return all_summary
# values = [1,2,3,4,5,6]
# more_values = [10,20,30,40,50,60]
# print(add_all(*values))             #"*" здесь используется тк в 2 строке *args является кортежем(неизменяемым списком).
#                                     # Поэтому для отображения обычного списка используется *values
# print(add_all(*values,*more_values))

# #2_вариант
# def autorize(**kwargs):
#
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#
# autorize(name='Sergey', age='28', job='QA')

#3_вариант
def autorize(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

date = {'Name:': 'Sergey', 'Age:': '28', 'Job:': 'QA'}
autorize(**date)



