#7) Fazer um algoritmo usando fluxograma para uma calculadora que faça as quatro operações básicas: +, -, * e /. 

valor1 = float(input('informe o valor:'))
operador = input('informe o operador (+,-,*,/):')
valor2 = float(input('informe o valor:'))
if (operador == '+'):
    resultado = valor1 + valor2
elif (operador == '-'):
    resultado = valor1 - valor2
elif (operador == '*'):
    resultado = valor1 * valor2
elif (operador == '/'):
    resultado = valor1 / valor2

print ('resultado:', resultado)