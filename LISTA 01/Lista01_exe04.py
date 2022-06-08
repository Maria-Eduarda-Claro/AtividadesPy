#Escrever um algoritmo  que calcule e imprima a quantidade de litros de  combustível gastos em uma viagem. Para isso, o usuário deverá fornecer o tempo gasto na  viagem e a velocidade média durante a mesma.  
#Observação, o automóvel utilizado faz 12 Km por litro.  
#- Distância = Tempo * Velocidade 
#- Litros Usados = Distância / 12 

tempo_gasto = float(input('Informe o tempo gasto na viagem:'))
velocidade_media = float(input('Informe a velocidade media:'))

distancia = (tempo_gasto * velocidade_media)
litros = (distancia/12)

print('a quantidade de litros gastos na viagem eh de:', litros)

