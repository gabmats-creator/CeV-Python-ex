import math
a = int(input('Digite um número: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print('O ângulo {}° tem: \nseno {:.2f} \n45cosseno {:.2f} \ntangente {:.2f}'.format(a, s, c, tg))
