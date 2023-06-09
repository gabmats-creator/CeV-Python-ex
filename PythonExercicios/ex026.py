n = str(input('Digite uma frase: ')).strip().lower()
print('A letra "a" aparece {} vezes sendo a primeira na posição {} e a última na posição sendo {}'.format(n.count('a'), n.find('a'), n.rfind('a')))