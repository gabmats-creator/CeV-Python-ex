class Alunos:
    def __init__(self):
        self.ra = None
        self.nome = None
        self.cpf =None
        self.curso = None
        self.idade = None
    def atribuir_ra(self, ra):
        self.ra = ra
    def atribuir_nome(self, nome):
        self.nome = nome
    def atribuir_cpf(self, cpf):
        self.cpf = cpf
    def atribuir_curso(self, curso):
        self.curso = curso
    def atribuir_idade(self, idade):
        self.idade = idade
    def atribuir_tudo(self, ra, nome, cpf, curso, idade):
        self.ra = ra
        self.nome = nome
        self.cpf = cpf
        self.curso = curso
        self.idade = idade
    def acessar_ra(self):
        return self.ra
    def acessar_nome(self):
        return self.nome
    def acessar_cpf(self):
        return self.cpf
    def acessar_curso(self):
        return self.curso
    def acessar_idade(self):
        return self.idade
    def maioridade(self):
        if self.idade >=18:
            return f'O(a) aluno {self.nome} é maior de idade'
        else:
            return f'O(a) aluno {self.nome} é menor de idade'
    def imprimir_dados(self):
        print(f'O(a) aluno(a) {self.nome} de RA {self.ra}, e cpf {self.cpf} tem {self.idade} anos e está matriculado(a) no curso {self.curso}')

class TabHash:
    def __init__(self, tamanho):
        self.tabela_hash = [None] * tamanho
        self.tamanho = tamanho
    def funcao_hash(self, nome):
        return len(nome) % self.tamanho

    def insert(self, aluno):
        nome = aluno.acessar_nome()
        indice = self.funcao_hash(nome)
        if self.tabela_hash[indice] is None:
            self.tabela_hash[indice] = nome
        else:
            zona_colisoes = 23
            if self.tabela_hash[zona_colisoes] is None:
                self.tabela_hash[zona_colisoes] = nome
            else:
                while self.tabela_hash[zona_colisoes] is not None:
                    if zona_colisoes < 29:
                        zona_colisoes +=1
                self.tabela_hash[zona_colisoes] = nome

    def search(self, nome):
        indice = self.funcao_hash(nome)
        if self.tabela_hash[indice] == nome:
            return indice
        else:
            for i in range(23, len(self.tabela_hash)):
                if self.tabela_hash[i] == nome:
                    return i
            return None

    def mostrar(self):
        # Esse tipo de for, printa o elemeto do índice e o índice propriamente dito
        for i, vet in enumerate(self.tabela_hash):
            print(i, vet)

    def remove(self, aluno):
        nome = aluno.acessar_nome()
        disponivel = 'd'
        if nome in self.tabela_hash:
            indice = self.funcao_hash(nome)
            if self.tabela_hash[indice] == nome:
                self.tabela_hash[indice] = disponivel
            else:
                for i in range(23, len(self.tabela_hash)):
                    if self.tabela_hash[i] == nome:
                        self.tabela_hash[i] = disponivel
                return None


aluno1 = Alunos()
aluno1.atribuir_nome('Gabriel')
aluno2 = Alunos()
aluno2.atribuir_nome('Anna')
aluno3 = Alunos()
aluno3.atribuir_nome('Yan')
aluno4 = Alunos()
aluno4.atribuir_nome('Rafaela')#1°Colisão
aluno5 = Alunos()
aluno5.atribuir_nome('Jorge')
aluno6 = Alunos()
aluno6.atribuir_nome('Maria')#2°Colisão
aluno7 = Alunos()
aluno7.atribuir_nome('João')#3°Colisão
aluno8 = Alunos()
aluno8.atribuir_nome('Mariele')#4°Colisão
aluno9 = Alunos()
aluno9.atribuir_nome('Alessandra')
aluno10 = Alunos()
aluno10.atribuir_nome('Rafael')
tab1 = TabHash(30)
tab1.insert(aluno1)
tab1.insert(aluno2)
tab1.insert(aluno3)
tab1.insert(aluno4)
tab1.insert(aluno5)
tab1.insert(aluno6)
tab1.insert(aluno7)
tab1.insert(aluno8)
tab1.insert(aluno9)
tab1.insert(aluno10)

tab1.remove(aluno1)
tab1.remove(aluno2)
tab1.remove(aluno3)
tab1.remove(aluno7)
tab1.remove(aluno8)

print(tab1.search('Jorge'))
print(tab1.search('Rafael'))
print(tab1.search('Maria'))
print(tab1.search('Geraldo'))