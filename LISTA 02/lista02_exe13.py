#13. Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo usando
#fluxograma para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros
#ele conseguiu colocar no tanque.

valor_do_litro = float(input('informe o valor do litro da gasolina:'))
valor_do_pagamento = float(input('informe o valor total pago:'))

total_litros = valor_do_pagamento / valor_do_litro

print('o total de litros abasecidos eh de:', total_litros)