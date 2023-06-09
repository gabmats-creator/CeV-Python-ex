class Produto:
    def __init__(self):
        self.name = None
        self.value = None
        self.describe = None

    def atribui_name(self, name):
        self.name = name

    def atribui_value(self, value):
        self.value = value

    def atribui_describe(self, describe):
        self.describe = describe

    def atribuir_all(self, name, value, describe):
        self.name = name
        self.value = value
        self.describe = describe

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_describe(self):
        return self.describe

    def get_all(self):
        print('O item é {}, {}, custa {}'.format(self.name, self.describe, self.value))

def main():
    produto = Produto()

    name = input("Digite o nome do produto: ")
    produto.atribui_name(name)

    value = float(input("Digite o valor do produto: "))
    produto.atribui_value(value)

    describe = input("Digite a descrição do produto: ")
    produto.atribui_describe(describe)

    print("\nInformações do produto:")
    print("Nome:", produto.get_name())
    print("Valor:", produto.get_value())
    print("Descrição:", produto.get_describe())

    produto.get_all()


main()
