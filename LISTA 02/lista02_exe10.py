#10. Faça um algoritmo usando fluxograma que pergunte a distância que um passageiro deseja
#percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para
#viagens até 200Km e R$0.45 para viagens mais longas

distancia = float(input('informe a distancia desejada:'))

if distancia  <=200:
    distancia = distancia * 0.50
elif distancia >200:
    distancia = distancia * 0.45

print('o valor da passagem eh:', distancia)
