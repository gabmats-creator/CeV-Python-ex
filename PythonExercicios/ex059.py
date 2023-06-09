n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
comando = 0
while comando != 5:
    comando = int(input(('Escolha uma opção:'
               '\n[1] Somar'
          '\n[2] Multiplicar'
          '\n[3] Maior'
          '\n[4] Novos números'
          '\n[5] Sair do programa'
                         '\n')))
    if comando == 1:
        print(n1 + n2)
    elif comando == 2:
        print(n1 * n2)
    elif comando == 3:
        if n1 > n2:
            print(f'O maior é {n1}')
        elif n1 <  n2:
            print(f'O maior é {n2}')
        else:
            print('Os dois valores são equivalentes.')
    elif comando == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif comando == 5:
        print('Fim da execução.')
    else: print('Comando inválido')
