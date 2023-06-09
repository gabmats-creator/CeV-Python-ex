#Atividade 1 aula 3
contpos = 0
contneg = 0
while True:
    n = int(input('Insira um número:'))
    if n <0:
        contneg += 1
    elif n == 0:
        break
    else:
        contpos += 1
print(f'Foram inseridos {contpos} números positivos e {contneg}')