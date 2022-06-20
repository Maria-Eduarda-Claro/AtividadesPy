#02 - Elabore um algoritmo que efetue o cálculo do reajuste de salário de um funcionário e
#imprima o novo salário. Considere que o funcionário deverá receber um reajuste de 15% caso
#o salário seja menor que R$ 500,00. Se o salário for maior ou igual a R$ 500,00 e menor ou
#igual a R$ 1.000,00, seu reajuste será de 10%, e caso seja ainda maior que R$ 1.000,00, o
#reajuste deverá ser de 5%.

salario_atual = float(input('informe o valor do seu salário atual:'))

if salario_atual <500:
    salario_atual += salario_atual *0.15
elif salario_atual <=1000:
    salario_atual+= salario_atual * 0.10
elif salario_atual > 1000:
    salario_atual += salario_atual * 0.5

print('seu novo salario eh:', salario_atual)
