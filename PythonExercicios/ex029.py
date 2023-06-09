n = float(input('Qual a velocidade atual do veículo? '))
if(n<80):
    print('Velocidade regular')
else:
    m = (n - 80)*7
    print('Você passou {:.2f}Km do limite e sua multa foi de R${:.2f}'.format(n - 80, m))
print('Tenha um bom dia, dirija com responsabilidade')