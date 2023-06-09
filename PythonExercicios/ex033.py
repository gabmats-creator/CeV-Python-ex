n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
menor = n1
if n2<n3 and n2<n1:
    menor = n2
if n3<n2 and n3<n1:
    menor = n3
maior = n1
if n2>n3 and n2>n1:
    maior = n2
if n3>n2 and n3>n1:
    maior = n3
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))