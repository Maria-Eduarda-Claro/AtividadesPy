#Desenvolver um algoritmo usando fluxograma que calcule e imprima o valor de uma  prestação em atraso, utilizando a seguinte fórmula:  
#Prestação = Valor + (Valor * (Taxa/100) * Tempo).   

valor_prestacao = float(input('informe o valor da prestacao em atraso:'))
tempo_em_atraso = float(input('informe a quanto tempo esta em atraso:'))
taxa = float(input('informe o valor da taxa:'))   #NÃO FOI INFORMADO O VALOR DA TAXA

calculo_prestacao = valor_prestacao + (valor_prestacao * (taxa/100) * tempo_em_atraso)
print (' O valor a pagar eh de:', calculo_prestacao)