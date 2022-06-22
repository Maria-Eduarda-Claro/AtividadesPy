def inserir_produto(lista):
    produto = input('informe o produto:')
    lista.append(produto)
    print('produto salvo com sucesso')

def pesquisar_produto(lista):
    achou = False
    produto = input('informe o produto:')
    for p in range(len(lista)):
        if (lista[p]== produto):
            print(p+1,'º -', lista[p])
            achou = True
    if not (achou):
        print('produto não localizado')
    input('pressione alguma tela para sair')

def excluir_produto(lista):
    achou = False
    produto = input('informe o produto:')
    for p in range(len(lista)):
        if (lista[p]==produto):
            del lista[p]
            achou = True
    if (achou):
        print('produto excluido com sucesso')
    else:
        print('produto não localizado')
    input('pressione alguma tela para sair')

def listar_produtos(lista):
    if range((len(lista)) >0):
        print('----- Lista de Produtos -----')
        for p in range(len(lista)):
            print(p+1,'º -'),lista[p]
    else:
        print('A lista está vazia')
    input('Pressione qualquer tecla para sair')



def menu():
    lista =[]
    opcao = 1
    while (opcao in (1,2,3,4)):
        print('1 - P/ Inserir produto')
        print('2 - P/ Pesquisar produto')
        print('3 - P/ Excluir produto')
        print('4 - P/ Listar todos os produtos')
        print('5 - P/ Sair')
        opcao = int(input('informe a opção:'))
        if (opcao ==1):
            inserir_produto(lista)
        elif (opcao ==2):
            pesquisar_produto(lista)
        elif (opcao ==3):
            excluir_produto(lista)
        elif (opcao ==4):
            listar_produtos(lista)
        
menu()
