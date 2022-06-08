#9) Fazer um algoritmo usando fluxograma que leia um valor, e apresente:  a) o próprio valor quando este for maior que 100;  
#b) exibi-lo multiplicado por (-1) quando este for menor que zero;  
#c) exibir a mensagem ‘nenhuma operação foi necessária’ em qualquer outra situação. 

valor = float(input('informe o valor:')) 

if (valor >100):
    print('valor:', valor)
elif (valor <0):
    print('valor', valor * -1)
else:
    print ('nenhuma operação foi necessária')
