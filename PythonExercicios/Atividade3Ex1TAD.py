from datetime import datetime
class Produto:
    def __init__(self):
        self.nome = None
        self.preco = None
        self.descricao = None

    def atribuir_nome(self, nome):
        self.nome = nome

    def atribuir_preco(self, preco):
        self.preco = preco

    def atribuir_descricao(self, descricao):
        self.descricao = descricao

    def atribuir_tudo(self, nome, value, describe):
        self.nome = nome
        self.preco = value
        self.descricao = describe

    def acessa_nome(self):
        return self.nome

    def acessa_preco(self):
        return self.preco

    def acessa_descricao(self):
        return self.descricao

    def acessa_tudo(self):
        print(f'O item é {self.nome}, {self.descricao}, custa R${self.preco}')

from datetime import datetime
class Carrinho:
    def __init__(self, name):
        self.name = name
        self.date = datetime.now().strftime('%d-%m-%Y')
        self.time = datetime.now().strftime('%H:%M:%S')
        self.itens = []

    def resgatar_tudo(self):
        return f'Cliente: {self.name}, carrinho criado em {self.date} às {self.time}'

    def add_produto(self, produto):
        self.itens.append(produto)

    def remove_produto(self, produto):
        if produto in self.itens:
            self.itens.remove(produto)

    def somatorio(self):
        products = []
        sum = 0
        for item in self.itens:
            nome = item.acessa_nome()
            preco = item.acessa_preco()
            descricao = item.acessa_descricao()
            if nome and preco and descricao:
                sum += preco
                products.append(f"O item é {nome}, {descricao}, custa R${preco}")
        return '\n'.join(products) + f'\nO valor total dos produtos é de R${sum}'

produto1 = Produto()
produto1.atribuir_tudo('Calça', 40.00, 'Calça Azul')

produto2 = Produto()
produto2.atribuir_tudo('Camiseta', 60.00, 'Camiseta Preta')
produto3 = Produto()
produto3.atribuir_tudo('Caneta', 2.00, 'Caneta bic esferográfica')

produto4 = Produto()
produto4.atribuir_tudo('Smartphone', 1200.00, 'Smartphone Xiaomi 5G')

carrinho = Carrinho('Gabriel')
carrinho.add_produto(produto1)
carrinho.add_produto(produto2)
carrinho.add_produto(produto3)
carrinho.add_produto(produto4)
carrinho.remove_produto(produto1)
print(carrinho.resgatar_tudo())
print(carrinho.somatorio())





