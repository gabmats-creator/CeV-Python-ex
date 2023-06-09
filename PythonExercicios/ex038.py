n1 = int(input(('Digite um número inteiro: ')))
n2 = int(input('Digite outro número inteiro: '))
if n1>n2:
    print('O menor número é {}, já o maior é {}'.format(n2, n1))
elif n1<n2:
    print('O menor número é {}, já o maior é {}'.format(n1, n2))
else:
    print('Não há maior, ambos são iguais')