n = int(input('Insira um número para calcular o seu fatorial: '))
repeticao = n
f = 1
while repeticao > 0:
    print(f'{repeticao}', end = '')
    print(' x 'if repeticao > 1 else ' = ', end = '')
    f*= repeticao
    repeticao -=1
print(f'{f}')