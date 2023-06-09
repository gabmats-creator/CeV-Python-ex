n = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão da P.A: '))
decimo = n + (10-1) * raz
for i in range(n, decimo + raz, raz):
    print('{}'.format(i), end='-> ')
print('Acabou')