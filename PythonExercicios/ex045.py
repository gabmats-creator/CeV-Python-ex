from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('Suas opções:')
print('[ 0 ] para PEDRA'
      '\n[ 1 ] para PAPEL'
      '\n[ 2 ] para TESOURA')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('O computador jogador {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
      if jogador == 0:
            print('Empate')
      elif jogador == 1:
            print('Jogador venceu')
      elif jogador == 2:
            print('Computador venceu')
      else:
            print('Opção inválida')
elif computador == 1:
      if jogador == 0:
            print('Computador venceu')
      elif jogador == 1:
            print('Empate')
      elif jogador == 2:
            print('Jogador venceu')
      else:
            print('Opção inválida')

elif computador == 2:
      if jogador ==0:
            print('Jogador venceu')
      elif jogador == 1:
            print('Computador venceu')
      elif jogador == 2:
            print('Empate')
      else:
            print('Opção inválida')
