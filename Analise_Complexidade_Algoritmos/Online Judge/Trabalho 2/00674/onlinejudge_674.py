def cacheVazio (qtdLinhas, qtdColunas):
  matriz = []
  linha = []
   
  ##Matriz de cache
  ##Linhas = VALORES
  ##Colunas = MOEDAS

  for c in range((qtdColunas)):
    linha.append(0)
  
  for l in range((qtdLinhas + 1)):
    matriz.append(linha.copy())
  
  return matriz

moedas = [1, 5, 10, 25, 50]

def quantidadeManeiras(valor, qtdMoedas):
  
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

      ##inicializa caso base - retornar qualquer valor com 0 moedas, tem somente 1 forma 
      for i in range(qtdTiposMoedas):
        cache[0][i] = 1

      for v in range(len(valores)):
        print(quantidadeManeiras(valores[v], qtdTiposMoedas))
        
      #print("")

      break
      
    valores.append(int(valor))

  except EOFError:
    break

