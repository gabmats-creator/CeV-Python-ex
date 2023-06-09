n = float(input('Qual é a distância a percorrer? '))
print('Você está prestes a realizar uma viagem de {:.2f}Km'.format(n))
if(n<=200):
    v = 0.5 * n
else:
    v = 0.45 * n
print('O valor da passagem foi de R${:.2f}'.format(v))