from datetime import date
a = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - a
if idade < 18:
    print('Você possui {} anos, portanto ainda faltam {} anos para você se alistar'.format(idade, 18 - idade))
    print('Seu alistamento será em {}'.format(a + 18))
elif idade == 18:
    print('Você possui 18 anos, está no período de se alistar!!')
else:
    print('Você possui {} anos, ja passou {} anos da idade, precisa procurar uma junta militar imediatamente'.format(idade, idade - 18))