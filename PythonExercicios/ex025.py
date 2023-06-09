n = str(input('Qual é o seu nome? ')).strip()
print('Seu nome é {}'.format(n.title()))
print('Possui Silva no nome? {}'.format('Silva' in n.title()))