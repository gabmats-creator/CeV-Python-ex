from datetime import date
n = int(input('Digite o ano de nascimento do nadador: '))
ano = date.today().year
idade = ano - n
if idade <= 9:
    print('Categoria mirim')
elif idade <= 14:
    print('Categoria infantil')
elif idade <= 19:
    print('Categoria Júnior')
elif idade <= 25:
    print('Categoria sênior')
else:
    print('Categoria master')
