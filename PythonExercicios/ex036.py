c = float(input('Digite o valor da casa: R$'))
s = float(input('Digite o seu salário: '))
a = int(input('Em quantos anos deseja pagar? '))
p = c/(a*12)
if p > s*0.30:
    print('Para comprar uma casa de R${:.2f} em {} anos, a prestação mensal será de R${:.2f}, portanto o empréstimo não será aprovado'.format(c, a, p))
else:
    print('Para comprar uma casa de R${:.2f} em {} anos, a prestação mensal será de R${:.2f}, empéstimo aprovado'.format(c, a, p))