from random import randint
from time import sleep
n = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente acertar!')
print('-=-'* 20)
n1 = int(input('Escolha um número de 0 a 5: '))
print('Processando...')
sleep(3)
if(n == n1):
    print('Parabéns, você me venceu')
else:
    print('Uma pena, tente novamente')
print