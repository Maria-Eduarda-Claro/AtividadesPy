#18. Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não.Para
#estar em condições, um dos seguintes requisitos deve ser satisfeito:

codigo_do_empregado = float(input('informe o codigo do empregado:'))
ano_de_nascimento = float(input('informe seu ano de nascimento:'))
ano_atual = float(input('informe o ano atual:'))
ano_de_ingresso = float(input('informe o ano de ingresso na empresa:'))

tempo_de_serviço = ano_atual - ano_de_ingresso
idade = ano_atual -ano_de_nascimento

if idade >= 65:
    print('requerer aposentadoria')
elif tempo_de_serviço >=30:
    print('requerer aposentadoria')
elif(idade >= 65) and (tempo_de_serviço >= 30):
    print('requerer aposentadoria')
else:
    print('não requerer aposentadoria')

   
