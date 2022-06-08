#Escrever um algoritmo usando fluxograma que leia o código do item pedido, a quantidade e  calcule o valor a ser pago por aquele lanche.  

quantidade = int(input('informe quantos lanches você irá pegar:'))
codigo_lanche = int(input('digite o codigo do lanche:'))

if quantidade>=2:
    codigo_lanche * quantidade
    codigo_lanche = int(input('digite o codigo do lanche:'))
if codigo_lanche ==100:
    preco_venda = 1.20
elif codigo_lanche == 101:
    preco_venda = 1.30
elif codigo_lanche == 102:
    preco_venda = 1.50
elif codigo_lanche ==103:
    preco_venda = 1.20
elif codigo_lanche ==104:
    preco_venda = 1.30
elif codigo_lanche ==105:
    preco_venda = 1.00
else:
    preco_venda = 0

valor_total = preco_venda * quantidade
print ('O valor total da compra eh:',valor_total)
