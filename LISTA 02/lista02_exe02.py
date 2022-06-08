#2. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem
#do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do
#distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo usando fluxograma que
#leia o custo de fábrica de um carro e escreva o custo ao consumidor.

custo_fabrica = float(input('informe o custo de fabrica do seu carro:'))

imposto = 45* custo_fabrica/100
distribuidor = 28* custo_fabrica/100

custo_total = custo_fabrica + imposto + distribuidor
print('o valor total do carro eh:', custo_total)