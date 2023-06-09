idades = 0
maior_idade = 0
mul_menores = 0
for i in range(1, 5):
    print('-' * 5, f'{i}° Pessoa', '-' * 5)
    nome = input(f'Qual o nome da {i}° pessoa? ').strip().title()
    idade = int(input(f'Qual a idade da {i}° pessoa? '))
    sexo = input(f'Qual o sexo da {i}° pessoa (M ou F)? ').strip().title()
    idades += idade
    if sexo == 'M':
        if sexo == 'M' and i == 1:
            maior_idade = idade
        if sexo == 'M' and idade > maior_idade:
            maior_idade = idade
            nome_velho = nome
    if sexo == 'F' and idade < 20:
         mul_menores +=1
print(f'Há {mul_menores} mulheres menores de 20 anos')
print(f'A média de idade das pessoas é de {idades/4}')
print(f'O homem mais velho tem {maior_idade} anos e se chama {nome_velho}')