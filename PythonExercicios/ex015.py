n = float(input('Quantos dias quilômetros o carro percorreu? '))
m = float(input('Por quantos dias o carro foi alugado? '))
p = 60*m + 0.15*n
print('O carro foi alugado por {:.1f} dias e percorreu {:.2f}Km, portanto o valor a ser pago é de R${:.2f}'.format(m, n, p))