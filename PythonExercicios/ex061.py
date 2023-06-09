n = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão da P.A: '))
pa = n
repeticao = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while repeticao <=total:
        print(f'{n}', end=' ')
        n += raz
        repeticao += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')

