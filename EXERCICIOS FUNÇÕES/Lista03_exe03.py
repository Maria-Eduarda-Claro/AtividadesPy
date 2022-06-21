#03 - Fulano tem 1,50 metro e cresce 2 centímetros por ano, enquanto Ciclano tem 1,10 metro
#e cresce 3 centímetros por ano. Construa um algoritmo que calcule e imprima quantos
#anos serão necessários para que Ciclano seja maior que Fulano.

def incrementar_altura( altura, incremento):
    return altura + incremento

fulano = 1.5
ciclano = 1.1
anos = 0
while(fulano >= ciclano):
    fulano = incrementar_altura (fulano, 0.02)
    ciclano = incrementar_altura (ciclano, 0.03)
    anos += 1

print(anos)
