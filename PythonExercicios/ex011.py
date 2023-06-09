l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
ar = l*a
t = ar/2
print('Uma parede com {:.2f}m de largura e {:.2f}m de altura, tem {:.2f}m de área e necessita de {:.2f} litros de tinta'.format(l, a, ar, t))