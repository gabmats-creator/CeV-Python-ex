p = float(input('Informe seu peso em Kg: '))
a = float(input('Informe sua altura em metros: '))
imc = p / (pow(a,2))
if imc < 18.5:
    print('Você está abaixo do peso, imc {:.2f}'.format(imc))
elif 18.5 <= imc < 25:
    print('Peso ideal, imc {:.2f}'.format(imc))
elif 25 <= imc < 30:
    print('Sobrepeso, imc {:.2f}'.format(imc))
elif 30 <= imc < 40:
    print('Obesidade, imc {:.2f}'. format(imc))
else:
    print('Obesidade mórbida, imc {:.2f}'.format(imc))