def maior_lado_quadrado_possivel(qtd_linhas, qtd_colunas):
  #O problema considera um ponto central de busca, expandindo nível a nível
  #logo somente existirão quadrados com lados ímpares
  menor = qtd_linhas
  if qtd_colunas < menor:
    menor = qtd_colunas
  
  if menor % 2 == 1:
    return menor
  else:
    return menor - 1

def pesquisa(maior_lado_possivel, grid, x, y, qtd_linhas, qtd_colunas):
  c = 0
  maior_lado = 1
  valor_coordenada_busca =  grid[x][y]
  #print("Busca {}".format(valor_coordenada_busca)) ###################
  for l in range(maior_lado_possivel):
    if (l+1) % 2 == 1 and (l+1) != 1:
      c += 1
      #print("tamanho {}".format(l+1)) ##################
      verificou_todas_coordenadas = True
      for xb in range(x-c,x+c+1):
        #verificou_todas_coordenadas = True
        for yb in range(y-c,y+c+1):
          if not(xb == x and yb == y):
            #print("({},{},{},{})".format(xb,yb,grid[xb][yb],verificou_todas_coordenadas)) ################
            #Se encontrar um valor diferente ao redor 
            #ou for uma coordenada inexistente para
            if xb < 0 or yb < 0 or xb > qtd_linhas-1 or yb > qtd_colunas-1 or valor_coordenada_busca != grid[xb][yb]:
              verificou_todas_coordenadas = False
              break
      if verificou_todas_coordenadas:
        maior_lado = l+1

  return maior_lado

#INPUT DE DADOS
num_testes = -1

while num_testes < 0 or num_testes > 20:
  num_testes = int(input())

casos_teste = []
#####################################
## COMPOSICAO LISTA CASOS DE TESTE ##
## posicao 0: qtd linhas           ##
## posicao 1: qtd colunas          ##
## posicao 2: qtd_localizacoes     ##
## posicao 3: grid                 ##
## posicao 4: localizacoes         ##
#####################################
for t in range(num_testes):
  
  info_caso_teste = input()
  config_caso_teste = info_caso_teste.split(" ")

  qtd_linhas = int(config_caso_teste[0])
  qtd_colunas = int(config_caso_teste[1])
  qtd_localizacoes = int(config_caso_teste[2])

  #input string letras
  linhas_grid = []
  for l in range(qtd_linhas):
    linha = input()
    colunas_grid = []

    for c in range(len(linha)):
      colunas_grid.append(linha[c])

    linhas_grid.append(colunas_grid)

  localizacoes = []
  for lc in range(qtd_localizacoes):
    local = input()
    loc = local.split(" ")

    localizacoes.append([loc[0],loc[1]])

  casos_teste.append([qtd_linhas, qtd_colunas,qtd_localizacoes, linhas_grid, localizacoes])
  #print(linhas_grid)
  #print("--")

##PROCESSA O INPUT
for ct in range(num_testes):

  info_teste = casos_teste[ct]

  qtd_linhas = info_teste[0]
  qtd_colunas = info_teste[1]
  qtd_localizacoes = info_teste[2]
  grid = info_teste[3]
  localizacoes = info_teste[4]

  print("{} {} {}".format(qtd_linhas, qtd_colunas, qtd_localizacoes))

  maior_lado_possivel = maior_lado_quadrado_possivel(qtd_linhas,qtd_colunas)
  
  #Para cada localização informada no caso de teste
  for loc in range(len(localizacoes)):
    
    if maior_lado_possivel == 1:
      print("1")
    
    else:
      x = int(localizacoes[loc][0])
      y = int(localizacoes[loc][1])

      #caracter_central = grid[x][y]
      print(pesquisa(maior_lado_possivel, grid, x, y, qtd_linhas, qtd_colunas))
