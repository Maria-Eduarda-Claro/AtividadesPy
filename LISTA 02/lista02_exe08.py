#8. Escreva um algoritmo usando fluxograma que pergunte a velocidade de um carro. Caso
#ultrapasse 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba
#o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.

velocidade_do_carro = float(input('informe a velocidade do carro:'))
execesso = 0
multa = 0
if velocidade_do_carro > 80:
   excesso = velocidade_do_carro -80
   multa = excesso * 5
   print('excesso de velocidade detectado:', multa)
