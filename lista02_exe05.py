#5. Uma empresa concederá um aumento de salário aos seus funcionários, variável de acordo
#com o cargo, conforme a tabela abaixo. Faça um algoritmo usando fluxograma que leia o salário
#e o cargo de um funcionário e calcule o novo salário. Se o cargo do funcionário não estiver na
#tabela, ele deverá, então, receber 40% de aumento. Mostre o salário antigo, o novo salário e a
#diferença.
print('Codigo de cargos:')
print()
print('gerente:101')
print()
print('engenheiro:102')
print()
print('técnico:103')
print()

salario_atual = int(input('informe o salario atual:'))
cargo = float(input('informe o código do seu cargo:'))

if cargo == '101':
    novo_salario = salario_atual + (salario_atual * 10)/100
elif cargo == '102':
    novo_salario = salario_atual + (salario_atual *20 )/100
elif cargo == '103':
    novo_salario = salario_atual + (salario_atual * 30)/100
else:
    novo_salario = salario_atual + (salario_atual * 40)/100

print('o salario atual eh:', salario_atual)
print('o novo salario eh:', novo_salario)

diferenca = novo_salario-salario_atual
print('a diferença do salario eh:', diferenca)