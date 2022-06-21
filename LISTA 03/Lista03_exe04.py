#04 - Faça um algoritmo para calcular e imprimir os números de 1 a 30 da série abaixo:
#5,10,20,25,35,40,50,55

numero = -5
for i in range(1,31):
    if i %2 == 0:
        numero = numero +5
        print(numero)
    else:
        numero = numero +10
        print(numero)