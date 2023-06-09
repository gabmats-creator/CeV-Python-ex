l1 = int(input('Digite o primeiro lado: '))
l2 = int(input('Digite o segundo lado: '))
l3 = int(input('Digite o terceiro lado: '))
if l1 < l2+l3 and l2<l1+l3 and l3<l2+l1:
    if l1 == l2 == l3:
        print('Este triangulo é equilátero')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('Este triângulo é isóceles')
    elif l1 != l2 != l3:
        print('Este triângulo é escaleno')
else:
    print('As três retas não formam um triângulo')