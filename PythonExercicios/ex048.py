s = 0
contador = 0
for i in range(1, 501, 2    ):
    if i%3 ==0:
        s+=i
        contador+=1
print('A soma dos {} termos ímpares e divisíveis por 3 equivale a {}'.format(contador, s))
