def cacheVazio (qtdLinhas, qtdColunas):
  matriz = []
  linha = []
  for c in range((qtdColunas + 1)):
    linha.append(0)
  
  for l in range((qtdLinhas + 1)):
    matriz.append(linha.copy())
  
  return matriz


def quantidadeManeiras(valor, qtdMoedas):
  
  #cache = cacheVazio(valor,qtdMoedas)

  #caso base  
  for i in range(qtdMoedas):
    cache[0][i] = 1

  for i in range(valor+1):
    if i >= 1:
      cache[i][0] = cache[i-1][0]
      cache[i][1] = cache[i-1][0]
      cache[i][2] = cache[i-1][0]
      cache[i][3] = cache[i-1][0]
      cache[i][4] = cache[i-1][0]

    if i>= 5:
      cache[i][1] += cache[i-5][1]
      cache[i][2] += cache[i-5][1]
      cache[i][3] += cache[i-5][1]
      cache[i][4] += cache[i-5][1]

    if i>= 10:
      cache[i][2] += cache[i-10][2]
      cache[i][3] += cache[i-10][2]
      cache[i][4] += cache[i-10][2]

    if i>= 25:
      cache[i][3] += cache[i-25][3]
      cache[i][4] += cache[i-25][3]

    if i>= 50:
      cache[i][4] += cache[i-50][4]


  return cache[valor][qtdMoedas-1]

#INPUT DE DADOS
valores = []
qtdTiposMoedas = len([1, 5, 10, 25, 50])

while True:
  try:
    
    valor = input()

    if not valor:
      
      #PROCESSAMENTO
      cache = cacheVazio(max(valores),qtdTiposMoedas)

      for v in range(len(valores)):
        print(quantidadeManeiras(valores[v], qtdTiposMoedas))

      break
      
    valores.append(int(valor))

  except EOFError:
    break

