n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
[ 1 ] Para BINÁRIO
[ 2 ] Para OCTAGONAL
[ 3 ] Para HEXADECIMAL
[ 4 ] Para BINÁRIO P/ INTEIRO''')

opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O número {} em base binária é igual a: {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('O número {} em base octagonal é igual a: {}'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('O número {} em base hexadecimal é igual a: {}'.format(n, hex(n)[2:]))
elif opcao == 4:
    nb = input('Digite um número binário: ')
    print('O número binário {} em decimal se torna {}'.format(nb, int(nb, 2)))
else:
    print('Opção inválida')