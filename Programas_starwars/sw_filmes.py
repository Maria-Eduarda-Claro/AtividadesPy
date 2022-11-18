class Filme():
    def __init__(self, titulo, genero, ano):
      self.titulo = titulo
      self.genero = genero
      self.ano = ano

    def __repr__(self):
      return 'titulo: {}, genero: {}, ano: {}' .format(self.titulo, self.genero, self.ano)

filmes = []
filmes.append(Filme('A Ameaça Fantasma - Episódio I', 'Ficcao',  '1999'))
filmes.append(Filme('Ataque dos Clones  - Episódio II', 'Ficcao',  '2002'))
filmes.append(Filme(' A Vingança dos Sith - Episódio III', 'Ficcao',  '2005'))
filmes.append(Filme(' Uma Nova Esperança - Episódio IV ', 'Ficcao',  '1977'))
filmes.append(Filme(' O Império Contra-ataca - Episódio V  ', 'Ficcao',  '1980'))
filmes.append(Filme(' O Retorno de Jedi - Episódio VI  ', 'Ficcao',  '1983'))

for filme in filmes:
  print(filme)