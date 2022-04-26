valor = 350.00

idade = input("Informe a idade:")
idade = int(idade)
fumante = input ("Informe 0 para nao fumante e 1 para fumante:")
fumante = int (fumante)

if idade < 50 and fumante == 1:
    variacao =20
elif idade < 50 and fumante == 0:
    variacao =-5
elif idade >= 50 and fumante == 0:
    variacao =-15
else: 
    variacao =25 

valorVariacao = valor * variacao /100
valorFinal = valor + valorVariacao

print ('valor       =', valor)
print ('variacao    =', variacao)
print ('valor Variacao   =', valorVariacao)
print ('valor Final   =', valorFinal)




print (variacao)

    