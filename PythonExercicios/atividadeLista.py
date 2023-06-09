lista = []
for i in range(100, 401):
    lista.append(i)
for i in lista:
    if i%7 == 0:
        print(i, end =' ')
print('\n', lista)