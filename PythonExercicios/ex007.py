n1 = int(input('Qual é a primeira nota do aluno? '))
n2 = int(input('Qual é a segunda nota do aluno? '))
m = (n1+n2)/2
print('A média do aluno é de {:.1f}'.format(m))
if m<60 : (print('Se lascou'))
else: print('Parabéns, você foi aprovado')