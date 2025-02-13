a = {1, 2, 3, 2, 4, 5, 5, 2 }
b = set([1, 2, 3, 2, 4, 5, 5, 2 ])
c = set("Hello Sergei Pavlov")
d = list (set([1, 2, 3, 2, 4, 5, 5, 2 ]))  #из списка делаем множество, удаляя дублирующие значения. После обратно делаем список
f = set (range(10))
print(15 in f)                              #Показывает входит ли число в данный передел. Нет не входит
f.update('sega')                            # добавляет в множество F допольнительные буквы



print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(f, type(f))

e = frozenset([1, 2, 3, 2, 4, 5, 5, 2 ])  #set можно менять, но frozenset менять нельзя
print(e, type(e))