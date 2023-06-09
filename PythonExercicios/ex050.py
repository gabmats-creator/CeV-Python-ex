s = 0
c = 0
for i in range(1, 7 ):
    n = int(input('Digite o {} valor: '.format(i)))
    if n%2 == 0:
        s +=n
        c +=1
print('Nos valores informados, há {} valores pares e a soma deles equivale a {}'.format(c, s))