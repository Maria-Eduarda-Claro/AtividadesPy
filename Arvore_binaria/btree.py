from more_itertools import bucket


class NoArvore:
    def __init__(self, valor = 0 ):
        self.valor = valor
        self.esquerda = None
        self.direita = None       

    def __repr__(self) -> str:
        resultado = ""

        if self.direita!=None:
            resultado ="("+str(self.direita.valor) + ")"

        resultado += " <--" +str(self.valor) + " -->"

        if self.esquerda!=None:
            resultado += "("+str(self.esquerda.valor) + ")"

        
        return resultado

def insereNoArvore(raiz, valor):
    # Se a raiz e vazia, cria o no raiz
    if (raiz ==None):
        raiz = NoArvore(valor)
        return raiz

# Se a raiz ja existe, vamos alocar o valor
    if (raiz.valor > valor):
        raiz.direita = insereNoArvore(raiz.direita, valor)
    elif (raiz.valor < valor):
      raiz.esquerda = insereNoArvore(raiz.esquerda, valor)



    return raiz

def imprimirArvoreOrdenado(raiz):
    if (raiz != None):
        imprimirArvoreOrdenado(raiz.direita)
        print(raiz.valor)
        imprimirArvoreOrdenado(raiz.esquerda)

  #metodo que busca um valor na arvore
  # -> NoArvore significa que ira retornar um objeto da claase NoArvore   
def buscarNaArvore(raiz, chave) -> NoArvore:
    if raiz==None:
        return None
    
    if (raiz.valor == chave):
        return raiz
    
    if (raiz.valor>chave):
      return  buscarNaArvore(raiz.direita, chave)
    else:
        return buscarNaArvore(raiz.esquerda, chave)


raiz = NoArvore(8)
insereNoArvore (raiz, 3)
insereNoArvore (raiz, 10)
insereNoArvore (raiz, 1)
insereNoArvore (raiz, 6)
insereNoArvore (raiz, 14)


#imprimirArvoreOrdenado(raiz)
busca = buscarNaArvore(raiz, 16)
if (busca!=None):
    print(busca.valor)
else:
    print("Registro nao encontrado!")