#17. A fábrica de refrigerantes Meia-Cola vende seu produto em três formatos: lata de 350 ml,
#garrafa de 600 ml e garrafa de 2 litros. Se um comerciante compra uma determinada quantidade
#de cada formato, faça um algoritmo usando fluxograma para calcular quantos litros de
#refrigerante ele comprou.

valor_lata = 0.350
valor_garrafa = 0.600
valor_pet = 2

qnt_lata = float(input('informe a quantidade de latas compradas:'))
qnt_garrafa = float(input('informe a quantidade de garrafas compradas:'))
qnt_pet = float(input('informe a quantidade de pet comprada:'))

total_litros = (qnt_lata * valor_lata) + (qnt_garrafa * valor_garrafa) + (qnt_pet * valor_pet)

print('o total de litros de refrigerante foi de:', total_litros)