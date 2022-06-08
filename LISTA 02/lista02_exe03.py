#3. Tendo como dados de entrada a altura e o sexo de uma pessoa (M – masculino e F –feminino),
#construa um algoritmo usando fluxograma que calcule seu peso ideal, utilizando as seguintes
#fórmulas:
#- para homens: (72.7*altura)-58
#- para mulheres: (62.1*altura)-44.7

altura = float(input('informe a sua altura:'))
sexo = str(input('informe o seu sexo  M ou F'))

if sexo == 'M':
    peso_ideal = (72.7*altura)-58
elif sexo == 'F':
    peso_ideal = (62.1*altura)-44.7
else:
    peso_ideal = 0
    
print('Seu peso ideal eh:', peso_ideal)



