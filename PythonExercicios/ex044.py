print('{:=^40}'.format(' Lojas Gabriel '))
preco = float(input("Valor das compras: "))
print("Opções de pagamento: "
      "\n[ 1 ] À vista no dinheiro"
      "\n[ 2 ] À vista no cartão"
      "\n[ 3 ] em 2x no cartão"
      "\n[ 4 ] 3x ou mais no cartão")
opcao = int(input("Digite a opção de pagamento: "))
parc = 0
if opcao == 1:
    preco_novo = preco - (preco*0.10)
elif opcao ==2:
    preco_novo = preco - (preco*0.5)
elif opcao ==3:
    preco_novo = preco
    parc = (preco / 2)
    print("Sua compra será parcelada em 2 vezes de {} SEM JUROS".format(parc))
elif opcao == 4:
    prest = int(input("Quantas parcelas? "))
    preco_novo = preco + (preco*0.20)
    parc = (preco_novo / prest)
    print("Sua compra será parcelada em {} vezes de {:.2f} COM JUROS".format(prest, parc))
else:
    preco_novo = 0
    print("Opção inválida, selecione uma das opções")
print("Sua compra de {:.2f} vai custar {:.2f} no final".format(preco, preco_novo))
