menor = 0
maior = 0
tmp = 0
for i in range(1, 6):
    n = int(input(f'Informe o peso da {i}° pessoa: '))
    if i == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    else:
        menor = n

print(f'O maior peso é: {maior}, já o menor é {menor}')