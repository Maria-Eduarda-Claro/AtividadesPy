#11) Fazer um algoritmo usando fluxograma para apresentar os resultados da tabuada de um  número qualquer. 

tabuada = int(input('informe o numero:'))

for i  in range (20): #feito até a tabuada do 20, apenas para teste
    print('%d * %d = %d' % (tabuada, i+1, tabuada*(i+1)) )
