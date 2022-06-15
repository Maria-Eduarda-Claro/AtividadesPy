#16. A granja Frangolino possui um controle automatizado de cada frango da sua produção. No
#pé direito do frango há um anel com um chip de identificação; no pé esquerdo são dois anéis
#para indicar o tipo de alimento que ele deve consumir. Sabendo que o anel com chip custa
#R$4,00 e o anel de alimento custa R$3,50, faça um algoritmo usando fluxograma para calcular o
#gasto total da granja para marcar todos os seus frangos.

anel_com_identificaçao = 4.00
anel_alimentação = 3.50
quantidade_anel_identificaçao = 1
quantidade_anel_alimentaçao = 2 

quantidade_frangos = float(input('informe a quantidade de frangos:'))

valor_total_aneis_identificaçao = (quantidade_frangos * quantidade_anel_identificaçao) * anel_com_identificaçao

valor_total_aneis_alimentaçao = (quantidade_frangos * quantidade_anel_alimentaçao) * anel_alimentação

valor_total_aneis = valor_total_aneis_identificaçao + valor_total_aneis_alimentaçao

print('o gasto total da granja frangolino eh de:', valor_total_aneis)