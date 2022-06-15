#9. Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos
#para todos, mas especialmente para mulheres. Faça um algoritmo usando fluxograma que leia
#nome, sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo
#que:
#- Homens ganham 5% de desconto
#- Mulheres ganham 13% de desconto

nome = str(input('informe o seu nome:'))
sexo = str(input('informe seu sexo:'))
valor_compras = float(input('informe o valor total das suas compras:'))

if sexo == 'masculino':
   valor_compras = (5 * valor_compras)/100
elif sexo == 'feminino':
   valor_compras = (13 * valor_compras)/100

print('O valor total a pagar eh:', valor_compras)