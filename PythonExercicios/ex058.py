from random import randint
comp = randint(0, 10)
n = int(input('Tente adivinhar um número: '))
cont = 1
while comp != n:
    comp = randint(0, 10)
    n = int(input('Tentativa incorreta, tente novamente: '))
    cont+=1

print(f'Parabéns, você acertou com {cont} tentativas')