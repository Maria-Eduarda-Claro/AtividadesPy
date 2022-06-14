#7. A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
#um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
#sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

quantidade_de_km = float(input('informe a quantidade de quilometros rodados:'))
dias = float(input('informe a quantidade de dias que o carro foi alugado:'))

quantidade_de_km = quantidade_de_km * 0.20
dias = dias * 90

total_a_pagar = quantidade_de_km + dias

print('o total a pagar eh:', total_a_pagar)