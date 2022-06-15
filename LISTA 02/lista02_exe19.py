#19. Desenvolva um algoritmo usando fluxograma para ler 10 números. Todos os números lidos
#com valor inferior a 40 devem ser somados. Escreva o valor final da soma efetuada.

soma = 0 
for i in  range (1,11):
    numero = int(input('informe um numero:'))
if numero <40:
    soma = soma + numero
    
print(soma)