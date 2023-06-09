class Tabela_hash_nome:
  def __init__(self, tamanho):
    self.tabela_hash = [None] * tamanho
    self.tamanho = tamanho
  def hash_nome(self, nome):
    return len(nome)%self.tamanho

  def inserir(self, nome):
    i = self.hash_nome(nome)
    if self.tabela_hash[i] is None:
      self.tabela_hash[i] = [nome]
    else:
      self.tabela_hash[i].append(nome)
  def mostrar(self):
      #Esse tipo de for, printa o elemeto do índice e o índice propriamente dito
      for i, vet in enumerate(self.tabela_hash):
        print(i, vet)
 #  for vet in self.tabela_hash:
#    print(vet)

t = Tabela_hash_nome(23)
t.inserir('Fernando')
t.inserir('Amelia')
t.inserir('Matheus')
t.inserir('Bernardo')
t.inserir('Danilo')
t.inserir('Andressa')
t.inserir('Alessandra')
t.inserir('Alice')
t.inserir('Waldenir')
t.mostrar()