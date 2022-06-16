def subtrair(n1,n2):
    r = n1 - n2
    return r
                                                #CRIANDO FUNÇÕES 
def multiplicar(n1,n2):
    r = n1 * n2
    return r

def somar(n1,n2):
    r = n1 + n2
    return r

def dividir (n1, n2):
    r = n1 / n2
    return r 


x = int(input('informe o valor 1:'))
op = input('informe o operador [+,-,/,*]:')
y = int(input('informe o valor 2:'))
if (op == '+'):
    resultado = somar(x,y)
elif (op == '-'):
    resultado = subtrair(x,y)
elif (op == '/'):
    resultado = dividir(x,y)
elif (op == '*'):
    resultado = multiplicar(x,y)

print('resultado da operaçao:', resultado)