def processa(casos_teste):
  for ct in range(len(casos_teste)):
    bolsas = casos_teste[ct]
    #caso base: 1 bolsa por si só é 1 forma
    qtdPossibilidades = 1
    qtdAtual = 1

    #print("caso teste {}".format(ct))

    bolsas_iguais = [] #armazenará o conjunto de bolsas iguais
    lista_bolsas_iguais = [] #lista com todos os conjuntos de bolsas iguais

    for i in range(len(bolsas)):
      if i != 0:
        if bolsas[i] == bolsas[i-1]: #se a bolsa atual for igual a bolsa anterior
          qtdAtual += 1  #conta mais uma bolsa atual
        else:
          lista_bolsas_iguais.append(bolsas_iguais)
          bolsas_iguais = []
          qtdAtual = 1 #se for diferente inicializa um novo "tipo" de bolsa
          #print("bolsa atual {}".format(bolsas[i]))
          #print("bolsa anterior {}".format(bolsas[i-1]))
          #print("qtd atual {}".format(qtdAtual))
          #print("qtd possibilidades {}".format(qtdPossibilidades))
          #print("----")
      bolsas_iguais.append(bolsas[i])

      #a quantidade de possibilidades é o maior entre 
      #o contador do tamanho atual da bolsa a maior quantidade de possibilidades até o momento
      qtdPossibilidades = max(qtdAtual, qtdPossibilidades)
    
    #inclusão na lista de possibilidades do último conjunto de bolsas iguais
    lista_bolsas_iguais.append(bolsas_iguais)

    #print(lista_bolsas_iguais)
    print(qtdPossibilidades)
    #print(bolsas)

  #  for i in range(qtdPossibilidades):
  #    #print(bolsas[i])
  #    forma = []
  #    for j in range(len(lista_bolsas_iguais)):
  #      print(lista_bolsas_iguais[j])
  #      if len(lista_bolsas_iguais[j]) != 0:
  #        forma.append(str(lista_bolsas_iguais[j][-1]))
  #        lista_bolsas_iguais[j].pop()
  #    print(" ".join(forma))

    
    #percorre a lista ordenada de bolsas de forma que
    #para cada possibilidade identificada são feitas as combinações possiveis
    #sendo que o get de bolsas é feito avançando na lista e incrementando os saltos
    #de acordo com as quantidades de possibilidades
    for i in range(qtdPossibilidades):
      forma = []
      for j in range(i,len(bolsas), qtdPossibilidades):
        if j < len(bolsas):
          forma.append(str(bolsas[j]))
      print(" ".join(forma))      

    print("")

#[1,1,1,1],[2,2,2],[3,3],[4,4]
#3
#1 2 3 4
#1 2 3
#1 2 4

casos_teste = []

while True:

  n = int(input())
  
  bolsas = []

  #Fim das entradas e processamento
  if n == 0:
    
    #PROCESSA ENTRADAS
    processa(casos_teste)

    break

  lista_bolsas = input().split()

  for b in range(len(lista_bolsas)):
    bolsas.append(int(lista_bolsas[b]))

  bolsas.sort() #ordena por tamanho
  casos_teste.append(bolsas)

