n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A média do aluno é de {:.2f}'.format(m))
if m >= 70:
    print('Aluno aprovado!')
elif 50 <= m < 70:
    print('Aluno de recuperação')
else:
    print('Aluno reprovado')