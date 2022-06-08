#14) Fazer um algoritmo usando fluxograma apresentar todos os valores numéricos impares  situados na faixa de 1000 a 1500. 

from re import I


soma = 0
for i in range(1000, 1501):
    if ((i % 2) == 1):
        print (i)
        soma = soma + i

print ("soma dos impares:", soma)