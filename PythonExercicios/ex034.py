s = float(input('Qual o salário atual? '))
if s > 1250:
    ns = s + s*0.10
else:
    ns = s + s*0.15
print('O salário de R${:.2f}, com o reajuste passará a ser de R${:.2f}'.format(s, ns))