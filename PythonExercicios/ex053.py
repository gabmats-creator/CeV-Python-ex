s = input('Escreva uma palavra ou frase: ').upper().strip()
s1 = s.split()
junto = ''.join(s1)
inverso = junto[::-1]
'''for letras in range(len(junto)-1, -1, -1):
    inverso += junto[letras]'''
if inverso == junto:
    print('A palavra ou frase, é palíndroma')
else:
    print('A palavra ou frase, não é palíindroma')
