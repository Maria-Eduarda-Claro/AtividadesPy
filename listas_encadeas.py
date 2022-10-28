class pessoa:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco    

class noLista:
    def __init__(self, dado, proximo_no = None):
        self.dado = dado
        self.proximo_no = proximo_no

    def __repr__(self):
        return "%s -> %s" % (self.dado, self.proximo_no)

class listaEncadeada:
    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    def insereNoInicio(self, novoDado):
        novoDado = noLista(novoDado)
        novoDado.proximo_no = self.cabeca
        self.cabeca = novoDado

    def insereNoFinal(self,novoDado):
        assert self.cabeca, 'No interior precisa existir na lista.'
        novoNo = noLista(novoDado)
        novoNo.proximo_no = self.cabeca.proximo_no
        self.cabeca.proximo_no = novoNo

    def pesquisa(self, valor):
        atual = self.cabeca
        while atual !=None and atual.dado !=valor:
            atual =atual.proximo_no
            return atual

lista = listaEncadeada()
#print("Lista Encadeada Vazia:", lista)
lista.insereNoInicio(50)
#print("Lista Encadeada com um item:", lista)
lista.insereNoFinal(85)
lista.insereNoFinal(86)
print('Lista Encadeada com No no fim:', lista)