n = str(input('Digite seu nome completo: ')).strip()
b = n.split()
print('Seu nome é {} {}'.format(b[0], b[len(b)-1]))