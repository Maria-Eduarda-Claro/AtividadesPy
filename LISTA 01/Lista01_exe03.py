# Ler uma temperatura em graus Fahrenheit, desenvolver um algoritmo usando fluxograma para converter e imprimir a temperatura em graus Celsius.  
#Fórmula de conversão: Temperatura em Celsius = (Temperatura em Fahrenheit – 32)*(5 / 9).
temperatura = float(input('informe a temperatura em fahrenheit:'))

conversao = (temperatura - 32)*(5/9)
print('a temperatura em celsius eh:', conversao)