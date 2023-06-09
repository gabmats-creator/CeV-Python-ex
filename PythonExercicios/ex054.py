from datetime import date
atual = date.today().year
menor = 0
maior = 0
for i in range(1, 8):
    n1 = int(input(f'Digite o ano de nascimento da {i}° pessoa: '))
    idade = atual-n1
    if idade>=18:
        maior +=1
    else:
        menor +=1

print(f'Dentro desse grupo de 7 pessoas, {maior} são maiores de idade e {menor} são menores')