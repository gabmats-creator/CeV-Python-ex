print('_'*30)
print('Sequência de fibonacci')
print('_'*30)
t1= 0
t2 = 1
n = int(input('Quantos termos você quer mostrar? '))
print(f'{t1} - {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1+t2
    print(f' - {t3}', end='')
    t1 = t2
    t2 = t3
    cont +=1
