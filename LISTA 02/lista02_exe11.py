#11. Crie um algoritmo usando fluxograma que leia a idade de 10 pessoas, mostrando no final:
#a) Qual é a média de idade do grupo
#b) Quantas pessoas tem mais de 18 anos
#c) Quantas pessoas tem menos de 5 anos

i = 1
quantidade_pessoa_mais18 = 0
quantidade_pessoa_menos5 = 0
somaIdade = 0
for i in range (1,11):
 idade = int(input('qual sua idade?'))
 if idade > 18:
     quantidade_pessoa_mais18 = quantidade_pessoa_mais18 + 1
 elif idade < 5:
     quantidade_pessoa_menos5 = quantidade_pessoa_menos5 + 1
 somaIdade = somaIdade + idade
 i = i + 1
mediaIdade = somaIdade / 10
print('a media de idade é: ', mediaIdade)
print('a quantidade de pessoa maior de 18 é: ', quantidade_pessoa_mais18)
print('a quantidade de pessoa menor de 5 é: ', quantidade_pessoa_menos5)