#10#) Fazer um algoritmo usando fluxograma que leia quatro valores referentes a quatro notas  escolares de um aluno e imprimir uma mensagem dizendo que o aluno foi aprovado, se o  valor da média escolar for maior ou igual a 7.  
#Se o valor da média for menor que 7, solicitar a nota de exame, somar com o valor da média  e obter nova média. Se a nova média for maior ou igual a 5, apresentar uma mensagem  dizendo que o aluno foi aprovado em exame.  
#Se o aluno não foi aprovado, indicar uma mensagem informando esta condição. Apresentar  com as mensagens o valor da média do aluno, para qualquer condição.

nota1 = float(input('informe a nota 1:'))
nota2 = float(input('informe a nota 2:'))
nota3 = float(input('informe a nota 3 :'))
nota4 = float(input('informe a nota 4:'))

media = (nota1+nota2+nota3+nota4)/4

if (media >= 7):
    print ('aluno aprovado com media', media)
else:
    notaexame = float(input('informe a nota do exame:'))
    novamedia = (media + notaexame)/2
    if (novamedia >= 5):
        print ('aluno aprovado por exame com media', novamedia)
    else:
            print ('aluno reprovado com media:', novamedia)
    
