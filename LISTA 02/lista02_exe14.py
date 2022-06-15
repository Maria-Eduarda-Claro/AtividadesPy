#14. Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo
#vendida respectivamente por 10, 12 e 15 reais. Construa um algoritmo usando fluxograma em
#que o usuário forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma
#venda, e a máquina
#informe quanto será o valor arrecadado.

camiseta_P = float(input('informe a quantidade vendida de camisetas P:'))
camiseta_M = float(input('informe a quantidade vendida de camisetas M:'))
camiseta_G = float(input('informe a quantidade vendida de camisetas G:'))

valor_total = (camiseta_P * 10) + (camiseta_M *12) + (camiseta_G * 15)

print('o valor total arrecadado eh de:', valor_total)