def cacheVazio (qtdLinhas, qtdColunas):
  matriz = []
  linha = []
  for c in range((qtdColunas + 1)):
    linha.append(-1)
  
  for l in range((qtdLinhas + 1)):
    matriz.append(linha.copy())
  
  return matriz

#INPUT DADOS
qtd_testes = int(input())  

casos_teste = []


for t in range(qtd_testes):

  qtd_objetos = int(input())
  objetos = []

  for n in range(qtd_objetos):
    objeto = input().split(" ")
    preco = int(objeto[0])
    peso = int(objeto[1])

    objetos.append((preco,peso))

  qtd_pessoas = int(input())
  pessoas = []

  for g in range(qtd_pessoas):
    maior_pesso_pessoa = int(input())
    
    pessoas.append(maior_pesso_pessoa)

  casos_teste.append([qtd_objetos,objetos,pessoas])


#Solução recursiva 
# Retorna o maior valor que pode ser carregado pela pessoa, com limite de peso G
def melhorValorPessoa(limitePeso, itens, n):  #n= qtdItens

    cache = cacheVazio(n,limitePeso)

    # caso básico (sem peso ou sem itens)
    if limitePeso == 0 or n == 0:
        return 0
    if cache[n][limitePeso] != -1:
        return cache[n][limitePeso]
 
    # Se o peso do item N é maior que o peso máximo que a pessoa pode carregar 
    # então esse item não pode ser considerado
    if (itens[n-1][1] > limitePeso):
        cache[n][limitePeso] = melhorValorPessoa(limitePeso, itens, n-1)
        return cache[n][limitePeso]
    # Retorna o maior entre o elemento N incluído e o elemento N não incluído
    else:
        cache[n][limitePeso] = max(
                                  #elemento N incluído
                                  itens[n-1][0] + melhorValorPessoa(limitePeso - itens[n-1][1], itens, n-1),
                                  #elemento N não incluído
                                  melhorValorPessoa(limitePeso, itens, n-1)
                                )
        return cache[n][limitePeso]

#itens = [(60,10), (100,20), (120,30)]  #(preço: 0 / peso: 1)
#limitePeso = 50    #peso que pode ser carregado pela pessoa
#n = len(val)  #quantidade de itens
#print(melhorValorPessoa(limitePeso, itens, n))

#Para cada caso de teste
for t in range(len(casos_teste)):
  ##########################################
  # posição 0: quantidade de itens
  # posição 1: preço/valor de cada itens
  # posicao 2: limite de peso das pessoas
  ########################################## 

  qtd_itens = casos_teste[t][0]
  itens = casos_teste[t][1]
  pessoas = casos_teste[t][2]
  
  maior_valor = 0

  cachePessoa = {}

  #Para cada pessoa: pessoas[p]: limite de peso que ela pode carregar
  for p in range(len(pessoas)):
    
    if not cachePessoa.get(pessoas[p]):

      maior_valor_pessoa = melhorValorPessoa(pessoas[p], itens, qtd_itens)  
      cachePessoa[pessoas[p]] = maior_valor_pessoa

      maior_valor += maior_valor_pessoa

    else:

      maior_valor += cachePessoa[pessoas[p]]

  print(maior_valor)

