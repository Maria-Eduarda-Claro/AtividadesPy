#1. Faça uma função que calcula a potência A elevado a B. Informe os valores para valores
#A e B, considere valores inteiros (não use o operador **).

def expoente(x,y):
    resultado = x 
    for i in range (1,y):
        resultado = resultado * x
        
    return resultado 

x = int(input('informe o valor :'))
y = int(input('informe o expoente:'))

resultado = expoente(x,y)

print(resultado)



