#01 - As Casas Bacana maior loja de departamentos da cidade de Pesqueiro Alto precisa de um
#algoritmo que leia o total em valor das compras do cliente, a forma de pagamento (D –
#dinheiro e C – cheque) e o prazo, conforme a tabela abaixo:

valor_das_compras = float(input('Informe o valor total de compras:'))
forma_de_pagamento = str(input('informe a forma de pagamento (D - dinheiro e C - cheque:'))
prazo = float(input('informe o prazo de pagamento:'))

if forma_de_pagamento =='D':
    valor_das_compras -= valor_das_compras * 0.20
elif forma_de_pagamento == 'C' and prazo <=30:
    valor_das_compras += valor_das_compras *0.12
elif forma_de_pagamento == 'C'and prazo >=90:
    valor_das_compras += valor_das_compras *0.15

print(' o valor total eh:', valor_das_compras)




