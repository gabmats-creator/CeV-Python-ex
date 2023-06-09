class Alunos:
    def init(self):
        self.ra = None
        self.nome = None
        self.cpf =None
        self.curso = None
        self.idade = None
    def atribuir_ra(self, ra):
        self.ra = ra
    def atribuir_nome(self, nome):
        self.nome= nome
    def atribuir_cpf(self, cpf):
        self.cpf= cpf
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


class Turma:
    def __init__(self, codigo, curso, periodo, sala):
        self.codigo = codigo
        self.curso = curso
        self.periodo = periodo
        self.sala = sala
        self.alunos = []

    def acessar_dados(self):
        return f'Turma de código: {self.codigo}, do curso de {self.curso} do {self.periodo}° período, presente na sala {self.sala}'

    def inserir_aluno(self, aluno):
        aluno_formatado = str(aluno.acessar_curso()).title().strip()
        if aluno_formatado == str(self.curso).title().strip():
            self.alunos.append(aluno)

    def remove_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)

    def dados_alunos(self):
        itens = []
        for item in self.alunos:
            ra = item.acessar_ra()
            nome = item.acessar_nome()
            cpf = item.acessar_cpf()
            curso = item.acessar_curso()
            idade = item.acessar_idade()
            if ra and nome and cpf and curso and idade:
                itens.append(f'O(a) aluno(a) {nome} de RA {ra}, e cpf {cpf} tem {idade} anos e está matriculado(a) no curso {curso}')
        return 'Estão matriculados nesta sala:\n' + '\n'.join(itens)

    def menoridade(self):
        sum = 0
        for aluno in self.alunos:
            if aluno.acessar_idade() < 18:
                sum += 1
        return f'Há {sum} alunos menores de idade na turma'

aluno1 = Alunos()
aluno1.atribuir_tudo(124, 'Gabriel', 1294724, 'Ciência da Computação', 19)
aluno2 = Alunos()
aluno2.atribuir_tudo(123, 'Rafael', 1294725, 'Ciência da computação', 17)
aluno3 = Alunos()
aluno3.atribuir_tudo(122, 'Samuel', 1294726, 'Ciência da computação', 15)
aluno4 = Alunos()
aluno4.atribuir_tudo(121, 'José', 1294727, 'Ciência da computação', 27)
turma1 = Turma(12866, 'Ciência da computação', 6, 10)
turma1.inserir_aluno(aluno1)
turma1.inserir_aluno(aluno2)
turma1.inserir_aluno(aluno3)
turma1.inserir_aluno(aluno4)
print(turma1.acessar_dados())
print(turma1.dados_alunos())
print(turma1.menoridade())