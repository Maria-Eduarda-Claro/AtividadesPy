
class Personagem():
    
    def __init__(self, novoNome, novaFuncao, novoPlaneta, novoObjeto ):
      self.nome = novoNome                   
      self.funcao = novaFuncao
      self.planeta = novoPlaneta
      self.objeto = novoObjeto
       

luke = Personagem('luke', 'piloto', 'tatooine', 'sabre de luz')
leia = Personagem('leia', 'princesa', 'alderan', 'cabelo esquisito')
vader = Personagem('vader', 'comandante da frota imperial', 'tatooine', 'sabre de luz')
hanSolo = Personagem('hanSolo', 'contrabandita', 'corelia', 'arma')

print(luke.nome)
print(luke.funcao)
print(luke.planeta)
print(luke.objeto)

print(leia.nome)
print(leia.funcao)
print(leia.planeta)
print(leia.objeto)
    
print(vader.nome)
print(vader.funcao)
print(vader.planeta)
print(vader.objeto)

print(hanSolo.nome)
print(hanSolo.funcao)
print(hanSolo.planeta)
print(hanSolo.objeto)