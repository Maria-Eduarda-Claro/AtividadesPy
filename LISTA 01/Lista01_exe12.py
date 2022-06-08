#12) Fazer um algoritmo usando fluxograma para apresentar todos os valores numéricos pares  entre 1 e 10. No final imprimir a soma dos valores impressos. 
soma = 0
for i in range (1,11):
    if(i % 2 == 0):
        print(i)
        soma = soma + i

print(soma)
    
    