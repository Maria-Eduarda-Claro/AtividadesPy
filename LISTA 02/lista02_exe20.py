#20. Desenvolva um algoritmo usando fluxograma que gera a sequência de 10 números abaixo:
#3, 10, 9, 20, 15, 30, 21, 40, 27 e 50

for i in range (1,11):
if (i % 2 == 0):
   numero = i * 5
else:
   numero = i * 3
   
print(numero)