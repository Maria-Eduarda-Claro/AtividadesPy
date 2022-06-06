#13) João papo-de-pescador, homem de bem, quer controlar o rendimento do seu trabalho. Toda  vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do  estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João 
#precisa que você faça um algoritmo usando fluxograma que leia o peso de peixes, e verifique  se há excesso, se houver excesso deverá ser calculada a multa que João deverá pagar. 

peso_peixes = float(input('informe o peso dos peixes:'))

if (peso_peixes >50):
   excesso = (peso_peixes - 50)

   multa = 4 * excesso 
   print('João pescou mais que o permitido, por isso gerou multa', multa)

else:
   
   print('João pescou dentro das normas', peso_peixes)
    
