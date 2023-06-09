import math
def mostrar_primos(n):
    print(f'Números primos de 2 até {n}')
    for i in range(2, n+1):
        is_primo = True
        for j in range(2, int(math.sqrt(i))):
            if i != j and i % j == 0:
                is_primo = False
                break
        if is_primo:
            print(i, end = ' ')

mostrar_primos(10000)

