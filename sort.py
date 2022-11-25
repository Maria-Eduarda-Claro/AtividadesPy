lista = []
for i in range (1025):
    lista.append(i)


print(lista)

numero = int(input("Informe um número:"))

tamanhoLista = len(lista)

o = 0
while 0 <=tamanhoLista:
    metade = (o +tamanhoLista)//2
    if lista[metade] == numero:
        print("Numero encontrado:", numero)
        break
    else:
        if numero < lista[metade]:
            tamanhoLista = metade -1
        else:
            o = metade +1