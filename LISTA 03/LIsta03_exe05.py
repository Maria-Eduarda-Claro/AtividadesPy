#05 - Faça um algoritmo para calcular e imprimir os números de 1 a 15 da série abaixo:
#5,7,10,12,15,17,20

numero = 2
for i in range(1,16):
    if i %2 == 0:
        numero = numero +2
        print(numero)
    else:
        numero = numero +3
        print(numero)