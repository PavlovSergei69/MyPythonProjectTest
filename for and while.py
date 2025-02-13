a = 5
while a > 0:
    a = a-1
    print ('a все еще меньше 0')

b = 5
count = 0
while b > 0:
    count = count+1
    print(f'Попытка №{count}')
    print('b все еще больше 0')
    if count == 2:
        break                         #останавливает работу
        #continue                      #продолжает работу


c = 5
count = 0
while b > 0:
    count = count+1
    print(f'Попытка №{count}')
    print('b все еще больше 0')
    if count == 5:
        print(f'Уже попытка №{count}, пора остановиться')
        break