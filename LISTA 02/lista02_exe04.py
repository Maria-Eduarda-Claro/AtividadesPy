#4. Um usuário deseja um algoritmo usando fluxograma onde possa escolher que tipo de média
#deseja calcular a partir de 3 notas. Faça um algoritmo que leia as notas, a opção escolhida pelo
#usuário e calcule a média.
#1 - aritmética
#2 - ponderada (3,3,4)

n1 = float(input('informe a nota 1:'))
n2 = float(input('informe a nota 2:'))
n3 = float(input('informe a nota 3:'))

tipomedia = str(input('informe a media desejada (1- aritimetica ou 2- ponderada):'))

if tipomedia == '1':
    media = (n1 + n2 + n3)/3
elif tipomedia == '2':
    media = ((n1*3)+(n2*3)+(n3*4))/(3+3+4)

print('a media eh:', format(media,".2f")) #format '.2f para formatar a media e arredondar ela