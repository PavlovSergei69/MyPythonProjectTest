a = {1, 2, 3, 2, 4, 5, 5, 2 }
print(a, type(a))

b = set([1, 2, 3, 2, 4, 5, 5, 2 ])
print(b, type(b))

c = set("Hello Sergei Pavlov")
print(c, type(c))

d = list(set([1, 2, 3, 2, 4, 5, 5, 2 ]))  #из списка делаем множество, удаляя дублирующие значения. После обратно делаем список
print(d, type(d))


f = set(range(10))
print(f, type(f))

print(15 in f)                              #Показывает входит ли число в данный передел. Нет не входит
f.update('s')                            # добавляет в множество F допольнительные буквы
f.add(10)
print(f, type(f))

e = frozenset([1, 2, 3, 2, 4, 5, 5, 2 ])  #set можно менять, но frozenset менять нельзя
print(e, type(e))