#15. A lanchonete Delicia vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de
#queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo
#ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um algoritmo
#usando fluxograma em que o dono forneça a quantidade de sanduíches a fazer, e a máquina
#informe as quantidades (em quilos) de queijo, presunto e carne necessários para compra.

peso_queijo = 0.100
peso_presunto = 0.50
peso_hamburguer = 0.50

quantidade_de_sanduiches = float(input('informe a quantidade de sanduiches a fazer:'))

quantidade_kg_queijo = quantidade_de_sanduiches * peso_queijo
quantidade_kg_presunto = quantidade_de_sanduiches *peso_presunto
quantidade_kg_hamburguer = quantidade_de_sanduiches * peso_hamburguer

print('a quantidade de cada item eh de:', quantidade_kg_queijo, quantidade_kg_presunto, quantidade_kg_hamburguer)



