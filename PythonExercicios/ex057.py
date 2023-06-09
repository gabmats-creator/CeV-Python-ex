n = input('Digite o gênero [M/F]: ').strip().upper()[0]
while n not in 'MmFf':
    n = input('Dados inválidos, por favor digite M ou F: ').strip().upper()[0]
print(f'O gênero {n} foi registrado com sucesso.')