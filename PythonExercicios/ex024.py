n = str(input('Digite o nome da cidade: ')).strip()
print('O nome da cidade é {}'.format(n.title()))
b = n.split()
print('O nome começa com Santo? {}'.format('Santo' in b[0].title()))