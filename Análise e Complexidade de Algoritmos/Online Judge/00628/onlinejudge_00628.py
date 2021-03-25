from itertools import product

def produto(lista_palavras,num_posicoes):
  produto = []
  for p in product(lista_palavras, repeat=num_posicoes):
    produto.append(p)
  return produto

def get_posicoes_tralha(regra):
    posicoes_tralha = []
    pos = regra.find("#")
    posicoes_tralha.append(pos)
    
    #identifica as posições do # na regra
    for pt in range(regra.count("#")-1):
        pos = regra.find("#",pos+1)
        posicoes_tralha.append(pos)  
    return posicoes_tralha

def gera_sequencias_numericas_regra(regra):#produz as sequencias numericas
  reg = regra.replace("0",".")
  regras = []
  
  produto_cart_num = produto(["0","1","2","3","4","5","6","7","8","9"], reg.count("."))

  for pr in range(len(produto_cart_num)):
    c = 0
    regra_gerada = ""
    posicao_zero = reg.find(".")

    for pos in range(reg.count(".")):
      if c == 0:
        regra_gerada = reg[:posicao_zero] + produto_cart_num[pr][c] + reg[(posicao_zero+1):]
      else:
        regra_gerada = regra_gerada[:posicao_zero] + produto_cart_num[pr][c] + regra_gerada[(posicao_zero+1):]
  
      posicao_zero = regra_gerada.find(".",posicao_zero + 1)
      c += 1

      if regra_gerada.count(".") == 0:
        regras.append(regra_gerada)
      
  return regras

def gera_senhas_regras_tralha(lista_palavras,regra):
  senhas = []
  produto_cartesiano = produto(lista_palavras,regra.count("#"))
 
  for pr in range(len(produto_cartesiano)):
    c = 0
    senha = ""
    posicao_tralha = regra.find("#")
 
    for pos in range(regra.count("#")):
      if c == 0:
        senha = regra[:posicao_tralha] + produto_cartesiano[pr][c] + regra[(posicao_tralha+1):]
      else:
        senha = senha[:posicao_tralha] + produto_cartesiano[pr][c] + senha[(posicao_tralha+1):]
 
      posicao_tralha = senha.find("#",posicao_tralha + len(produto_cartesiano[pr][c]) - 1)
      c += 1

      if senha.count("#") == 0:
        senhas.append(senha)
      
  return senhas

while True:
  try:
    
    numeroPalavras = int(input())
    palavras = []

    for _ in range(numeroPalavras):
      palavras.append(input())

    print(palavras)
    
    numeroRegras = int(input())
    regras = []

    for _ in range(numeroRegras):
      regras.append(input())

    print(regras)

    print("--")
    
    for r in (range(len(regras))):
      senhas = []
      regras_expandidas = gera_sequencias_numericas_regra(regras[r])

      if regras[r].find("#") != -1:
        for i in range(len(regras_expandidas)):
          senhas.extend(gera_senhas_regras_tralha(palavras,regras_expandidas[i]))
      else:
        senhas.extend(regras_expandidas)
      
      senhas.sort()

      for j in range(len(senhas)):
        print(senhas[j])

  except EOFError:
    break