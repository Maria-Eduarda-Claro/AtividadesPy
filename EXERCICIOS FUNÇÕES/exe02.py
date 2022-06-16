#2. Escreva uma função que recebe dois valores e imprime o menor dos dois. Se eles forem
#i#guais, imprima que eles são iguais.

def exe02():
    x = int(input('informe o valor 1:'))
    y = int(input('informe o valor 2:'))

    if (x>y):
        print('o maior:', x)
    elif (x<y):
        print('o maior:', y)
    else:
        print('valores iguais')

exe02()                        #CHAMAR FUNÇÃO 

#COMO ESTOU CRIANDO UMA FUNÇÃO, PRECISO CHAMAR A MESMA PARA EXECUTAR, POIS ELA NÃO É AUTO EXECUTÁVEL. ESTA FUNÇÃO PODERIA ESTAR DENTRO DE ALGUM PROGRAMA ;o