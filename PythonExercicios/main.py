class No:
    def __init__(self, valor, anterior=None, proximo=None):
        self.valor = valor
        self.anterior = anterior
        self.proximo = proximo

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar(self, valor):
        novo_no = No(valor, self.fim, None)
        if self.fim:
            self.fim.proximo = novo_no
        self.fim = novo_no
        if not self.inicio:
            self.inicio = self.fim

    def remover(self, valor):
        atual = self.inicio
        while atual:
            if atual.valor == valor:
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.inicio = atual.proximo
                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.fim = atual.anterior
                return
            atual = atual.proximo

    def mostrar(self):
        atual = self.inicio
        resultado = []
        while atual:
            resultado.append(atual.valor)
            atual = atual.proximo
        return resultado

lista = ListaDuplamenteEncadeada()
for i in range(10):
    lista.adicionar(i)

for i in range(6, 10):
    lista.remover(i)

print(lista.mostrar())
