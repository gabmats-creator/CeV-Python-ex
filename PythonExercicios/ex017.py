import math
co = float(input('Qual a medida do cateto oposto? '))
ca = float(input('Qual a medida do cateto adjacente? '))
h = math.hypot(co, ca)
print('A medida da hipotenusa é de {:.2f}'.format(h))