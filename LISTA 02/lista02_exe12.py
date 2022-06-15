#12. A padaria Delicia Pão Doce uma certa quantidade de pães franceses e uma quantidade de
#broas a cada dia. Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia, o dono
#quer saber quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar
#numa conta de poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos
#para o dono. Com base nestes fatos, faça um algoritmo usando fluxograma para ler as
#quantidades de pães e de broas, e depois calcular os dados solicitados.

quantidade_paes = float(input('informe quantos pães foram vendidos:'))
quantidade_broas = float(input('informe a quantas broas foram vendidas:'))

valor_total = (quantidade_paes * 0.12) + (quantidade_broas * 1.50)
valor_poupanca = (valor_total * 10)/100

print('o valor total vendido foi de:', valor_total)
print('o percentual que deve ser guardado eh de:', valor_poupanca)

