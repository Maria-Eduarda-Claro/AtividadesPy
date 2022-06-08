#8) Fazer um algoritmo usando fluxograma que leia um valor inteiro, e informe através de uma  mensagem, se este valor é um número par ou ímpar.  

numero = int(input('informe um numero inteiro:'))

if (numero % 2) == 0:
    print ('o numero eh par')
else:
    print ('o numero eh impar')