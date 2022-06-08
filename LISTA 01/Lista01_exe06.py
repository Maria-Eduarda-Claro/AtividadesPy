#6) Desenvolver um algoritmo usando fluxograma para calcular e imprimar a média ponderada  de 3 notas (N1, N2, N3) com os respectivos pesos 2, 5 e 3 (P1, P2, P3). 
p1 = 2
p2 = 5
p3 = 3
N1 = float(input('informe a nota 1:'))
N2 = float(input('informe a nota 2:'))
N3 = float(input('informe a nota 3:'))

media = ((N1 * p1) + (N2 * p2) + (N3 * p3) / (p1+ p2 + p3))

print('media:', media)