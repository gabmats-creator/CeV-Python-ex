n1 = int(input('Digite o primeiro lado: '))
n2 = int(input('Digite o segundo lado: '))
n3 = int(input('Digtie o terceiro lado: '))
if n3 < n1+ n2 and n2 < n3 + n1 and n1 < n3 + n2:
    print('As três retas formam um triângulo')
else:
    print('As três retas não formam um triângulo')