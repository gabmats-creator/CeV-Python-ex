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
    def maioridade(self):
        if self.idade >=18:
            return f'O(a) aluno {self.nome} é maior de idade'
        else:
            return f'O(a) aluno {self.nome} é menor de idade'
    def imprimir_dados(self):
        print(f'O(a) aluno(a) {self.nome} de RA {self.ra}, e cpf {self.cpf} tem {self.idade} anos e está matriculado(a) no curso {self.curso}')

    # Cria um objeto da classe Alunos

def main():
    aluno1 = Alunos()
    # Atribui valores aos atributos do objeto
    aluno1.atribuir_tudo('12345', 'João', '123.456.789-00', 'Ciência da Computação', 20)
    # Imprime os dados do aluno
    aluno1.imprimir_dados()
    # Verifica se o aluno é maior de idade
    print(aluno1.maioridade())
    # Atribui novo valor ao atributo "curso"
    aluno1.atribuir_curso('Engenharia de Software')
    # Imprime novamente os dados do aluno
    aluno1.imprimir_dados()
    # Cria outro objeto da classe Alunos
    aluno2 = Alunos()
    # Atribui valores aos atributos do objeto
    aluno2.atribuir_tudo('67890', 'Maria', '987.654.321-00', 'Engenharia Civil', 25)
    # Imprime os dados do aluno
    aluno2.imprimir_dados()
    # Verifica se o aluno é maior de idade
    print(aluno2.maioridade())
if __name__ == "__main__":
    main()
