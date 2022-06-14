#6. Faça um algoritmo que leia a largura e altura de uma parede, calcule e
#mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura_parede = float(input('informe a largura da parede:'))
largura_parede = float(input('informe a altura da parede:'))

qnt_de_tinta = (altura_parede * largura_parede)/2

print('eh necessario:', qnt_de_tinta)
